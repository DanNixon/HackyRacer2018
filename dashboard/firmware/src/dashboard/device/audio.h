#pragma once

#include <string>
#include <vector>

#include <Audio.h>

#include "dashboard/value/numeric_units.hpp"

namespace dashboard
{
namespace device
{
  using FilenameList = std::vector<std::string>;

  enum AudioSource
  {
    AUDIO_SOURCE_HORN = 0,
    AUDIO_SOURCE_MUSIC = 1,
    AUDIO_SOURCE_ANNOUNCE = 2,
  };

  extern value::VolumeValue audioMusicVolume;
  extern value::VolumeValue audioHornVolume;

  void audioInit();
  void audioUpdate();

  void audioSetGain(AudioSource source, float gain);

  void audioHornOn();
  void audioHornOff();

  AudioPlaySdWav &audioMusic();
  const FilenameList &audioMusicFiles();
  size_t audioMusicNowPlaying();
  bool audioMusicPlaying();
  void audioMusicPlay(size_t idx = 0);
  void audioMusicPrevious();
  void audioMusicNext();
  void audioMusicStop();
}
}
