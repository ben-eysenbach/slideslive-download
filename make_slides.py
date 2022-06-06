import json
import os
with open('slides.json') as f:
  d = json.load(f)
with open('input.txt', 'wb') as f:
  for i, slide in enumerate(d['slides']):
    f.write('file \'%s.png\'\n' % slide['image']['name'])
    if i < len(d['slides']) - 2:
      duration = (d['slides'][i+1]['time'] - slide['time']) / 1000.0
    f.write('duration %f\n' % duration)
  f.write('file \'%s.png\'\n' % slide['image']['name'])

os.system('ffmpeg -f concat -i input.txt -vsync vfr -pix_fmt yuv420p -c:v libx264 -crf 0 slides.mp4')
