#include "horn.h"

#include <Bounce2.h>

#include "audio.h"
#include "pin_config.h"

namespace dashboard
{
namespace device
{
  Bounce hornButton;

  void hornInit()
  {
    pinMode(HORN_BUTTON_PIN, INPUT_PULLUP);

    hornButton.attach(HORN_BUTTON_PIN);
    hornButton.interval(20);
  }

  void hornUpdate()
  {
    hornButton.update();

    if (hornButton.fell())
    {
      /* Horn button pressed */
      audioHornOn();
    }
    else if (hornButton.rose())
    {
      /* Horn button released */
      audioHornOff();
    }
  }
}
}
