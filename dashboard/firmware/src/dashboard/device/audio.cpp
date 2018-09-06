#include "audio.h"

#include <SD.h>

namespace dashboard
{
namespace device
{
  constexpr auto FLANGE_DELAY_LENGTH(6 * AUDIO_BLOCK_SAMPLES);
  short flangeDelayline[FLANGE_DELAY_LENGTH];

  AudioSynthWaveform sourceHornTone;
  AudioEffectFlange effectHornFlange;
  AudioPlaySdWav sourceMusic;
  AudioPlaySdWav sourceAnnounce;
  AudioMixer4 mixerLeft;
  AudioMixer4 mixerRight;
  AudioOutputAnalogStereo outputDac;

  AudioConnection patchCord0(sourceHornTone, effectHornFlange);
  AudioConnection patchCord1(effectHornFlange, 0, mixerLeft, AUDIO_SOURCE_HORN);
  AudioConnection patchCord2(effectHornFlange, 0, mixerRight, AUDIO_SOURCE_HORN);
  AudioConnection patchCord3(sourceMusic, 0, mixerLeft, AUDIO_SOURCE_MUSIC);
  AudioConnection patchCord4(sourceMusic, 1, mixerRight, AUDIO_SOURCE_MUSIC);
  AudioConnection patchCord5(sourceAnnounce, 0, mixerLeft, AUDIO_SOURCE_ANNOUNCE);
  AudioConnection patchCord6(sourceAnnounce, 1, mixerRight, AUDIO_SOURCE_ANNOUNCE);
  AudioConnection patchCord7(mixerLeft, 0, outputDac, 0);
  AudioConnection patchCord8(mixerRight, 0, outputDac, 1);

  bool audioMusicShouldPlay(false);
  size_t audioMusicCurrentIdx(0);

  value::VolumeValue audioMusicVolume("Music");
  value::VolumeValue audioHornVolume("Horn");

  void audioInit()
  {
    /* For more information, see the MemoryAndCpuUsage example */
    AudioMemory(8);

    /* Horn */
    {
      sourceHornTone.begin(WAVEFORM_TRIANGLE);
      sourceHornTone.frequency(440);
      sourceHornTone.amplitude(0.0f);

      {
        constexpr int index(FLANGE_DELAY_LENGTH / 4);
        constexpr int depth(FLANGE_DELAY_LENGTH / 4);
        constexpr double freq(0.5);
        effectHornFlange.begin(flangeDelayline, FLANGE_DELAY_LENGTH, index, depth, freq);
      }
    }
  }

  void audioUpdate()
  {
    /* Handle music volume */
    if (audioMusicVolume.valueDirty(value::IValue::DIRTY_PARAMETER, true))
    {
      audioSetGain(AUDIO_SOURCE_MUSIC, audioMusicVolume.value());
    }

    /* Handle horn volume */
    if (audioHornVolume.valueDirty(value::IValue::DIRTY_PARAMETER, true))
    {
      audioSetGain(AUDIO_SOURCE_HORN, audioHornVolume.value());
    }

    /* Handle music */
    if (!audioMusicShouldPlay && sourceMusic.isPlaying())
    {
      sourceMusic.stop();
    }
    else if (audioMusicShouldPlay && !sourceMusic.isPlaying())
    {
      audioMusicNext();
    }
  }

  void audioSetGain(AudioSource source, float gain)
  {
    mixerLeft.gain(source, gain);
    mixerRight.gain(source, gain);
  }

  void audioHornOn()
  {
    sourceHornTone.amplitude(1.0f);
  }

  void audioHornOff()
  {
    sourceHornTone.amplitude(0.0f);
  }

  FilenameList audioListFiles(const char *dirname)
  {
    FilenameList files;
    File dir = SD.open(dirname);
    while (true)
    {
      File entry = dir.openNextFile();
      if (!entry)
      {
        break;
      }
      files.push_back(std::string(dirname) + std::string(entry.name()));
      entry.close();
    }
    return files;
  }

  AudioPlaySdWav &audioMusic()
  {
    return sourceMusic;
  }

  const FilenameList &audioMusicFiles()
  {
    static const FilenameList list(audioListFiles("/MUSIC/"));
    return list;
  }

  size_t audioMusicNowPlaying()
  {
    return audioMusicCurrentIdx;
  }

  bool audioMusicPlaying()
  {
    return audioMusicShouldPlay;
  }

  void doPlay()
  {
    sourceMusic.stop();
    audioMusicShouldPlay = true;
    sourceMusic.play(audioMusicFiles()[audioMusicCurrentIdx].c_str());
  }

  void audioMusicPlay(size_t idx)
  {
    audioMusicCurrentIdx = std::min(idx, audioMusicFiles().size() - 1);
    doPlay();
  }

  void audioMusicPrevious()
  {
    if (audioMusicCurrentIdx == 0)
    {
      audioMusicCurrentIdx = audioMusicFiles().size() - 1;
    }
    else
    {
      audioMusicCurrentIdx--;
    }

    doPlay();
  }

  void audioMusicNext()
  {
    audioMusicCurrentIdx++;
    if (audioMusicCurrentIdx == audioMusicFiles().size())
    {
      audioMusicCurrentIdx = 0;
    }

    doPlay();
  }

  void audioMusicStop()
  {
    audioMusicShouldPlay = false;
  }
}
}
