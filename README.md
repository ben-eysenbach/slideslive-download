# Slideslive Download.

Last updated June 6, 2022.

This page describes how to download a slideslive presentation. The output is a single video file that shows the speaker and slides side-by-side.

1. Install a Chrome extension that allows you to save the video resources: [Save All Resources](https://chrome.google.com/webstore/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb?hl=en)
   Restart your web-browser.
2. Navigate to the website hosting the slideslive presentation. Open the *Developer tools* and navigate to the far-right tab, titled *ResourcesSaver*.
3. Start playing your video. Wait until it is done playing.
4. In the *ResourcesSaver* tab, click *Save All Resources*. This includes all the relevant information to reconstruct the video, split into three types:
  * `init_3_*.m4s` and `chunk_3_*.m4s`: These store the speaker's video. 
  * `init_5_*.m4s` and `chunk_5_*.m4s`: These store the speaker's audio. 
  * `slides.json`: This is a simple json file indicating when each slide should be shown.
  * `*.png`: These are the slides.
   Copy the above files into a "flat" directory. You should now have a single folder with the ~100s of `m4s` files, ~10s of `png` files, and one `json` file.
5. Combine the m4s files into an mp4 video:
  ```
  cat init_3_*.m4s >> video.m4s
  cat chunk_3_*.m4s >> video.m4s

  cat init_5_*.m4s >> audio.m4s
  cat chunk_5_*.m4s >> audio.m4s

  ffmpeg -i video.m4s -i audio.m4s -c:v copy -c:a aac video.mp4
  ```
6. Make a video from the slides and JSON metadata file: `python make_slides.py`
7. Combine the speaker video and slide video into a single side-by-side video:
```
ffmpeg -i video.mp4 -i slides.mp4  -filter_complex '[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]' -map '[vid]' -map a:0 -c:v libx264 combined.mp4
```

----------------
These instructions are provided as-is, without any maintenance or ongoing support. If you have issues with these instructions, please submit a pull request.
