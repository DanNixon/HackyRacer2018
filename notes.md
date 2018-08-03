# Notes

## Rear axle

- Nut on non driven wheel can be tightened sufficiently to give some power
  transfer

## Steering column

- Adapted to make vertical (to avoid legs getting in the way)
- Needs a bushing between steering wheel and top of mount
  - 25mm for "normal" operation (i.e. steering operates between restricted range)
  - 16mm for extended operation (steering operates beyond restricted range, this
    can cause front tyres to get caught in front bumper, so maybe don't use it)
- Back of steering wheel is roughly 20mm across

## VESC control wiring

### VESC pinout

```
1 ADC2
2 RX
3 TX
4 ADC1
5 GND
6 3.3V
7 5V
```

### JST PH

Viewed with tabs on bottom.

```
^ ^ ^ ^ ^ ^ ^
1 2 3 4 5 6 7
| | | | | | |
```

### 0.1" header

Viewed from front.

```
  TX  3 4  ADC2
  RX  2 5  GND
ADC2  1 6  3.3v
 N/C  x 7  5V
```
