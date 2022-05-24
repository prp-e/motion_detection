# Motion Detection

## TODO

- [x] Testing on a Raspberry Pi (with USB camera)
- [ ] Testing on a Raspberry Pi (with IP Camera/Mobile Phone)
- [ ] Testing on a Raspberry Pi (with Raspberry Pi camera module)
- [ ] Moving things to [mediapipe](https://google.github.io/mediapipe)
    - [ ] Working on a _threat detection_ system.
- [x] Try to record a video every time a motion is captured.
- [ ] Change `video = VideoWriter('activities/' + datetime.now().strftime("%Y-%m-%d-%I-%M") + str(uuid4()) + '.avi', VideoWriter_fourcc(*'MJPG'), 24, (1280, 720))` to read the frame size from _frame_'s shape.
