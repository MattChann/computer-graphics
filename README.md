# Work 12: The End
## Matthew Chan, pd 5

Features:
- **set**
    - Assign a value to a specific knob or all knobs
    - ex: `set knob 5`
    - ex: `set_knobs 3`
- **saveknobs**
    - Save current knob values to a list
    - ex: `saveknobs list0`
- **tween**
    - Produce an animation by going between two knob lists
    - ex: `tween 0 10 list0 list1`
- **ease**
    - Change the behavior of transitioning knob values
    - Inspired by [GreenSock Easing](https://greensock.com/docs/v3/Eases)
    - Options: linear (default), power1, power2, power3, power4, back, elastic, bounce
    - Can be used with: `vary`, `tween`
    - ex: `vary knob 0 49 0 1 elastic`
    - ex: `tween 20 99 list0 list1 bounce`
