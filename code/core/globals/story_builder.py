from moviepy.editor import TextClip, ImageClip, CompositeVideoClip
from uuid import uuid4
from moviepy.video.fx.resize import resize
from moviepy.config import change_settings


class StoryBuilder:
    """
        Description :
            For building the user story depends on user input.

        Param:
            - text_list:list[dict]
                ex: 
                    [{
                        "content" : "content is here",
                        "color" : "red",
                        "x" : 10,
                        "y" : 30,
                    }]
            - image:
                the path of the image that will appear in the story

    """

    def __init__(self, text_list:list[dict], image):        
        self.text_list = text_list
        self.image = image
        change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})

    def build(self) : 
        story_size = (1080, 1920)
        elements = []
        
        fonts = TextClip.list('font')
        for txt in self.text_list :
            txt_clip = TextClip(txt['content'],fontsize=70, color=txt['color'], font=fonts[0])
            txt_clip = txt_clip.set_duration(30)
            txt_clip = txt_clip.set_position((txt['x'],txt['y']))
            
            elements.append(txt_clip)


        img_clip = ImageClip(self.image[1::]).set_duration(30).resize(height=story_size[1])  # Resize to fit height
        img_clip = img_clip.set_position(('center', 'center'))
        
        # img_clip = ImageClip(self.image[1::], duration=30)#.set_duration(30)#.resize(height=story_size[1])  # Resize to fit height
        # # img_clip = resize(img_clip, newsize=story_size)

        # img_clip = img_clip.resize(height=story_size[1])



        elements.insert(0, img_clip)

        video = CompositeVideoClip(elements, size=story_size)

        saved_path = f"media/stories/{uuid4()}.mp4"
        video.write_videofile(saved_path, fps=24)
        return saved_path



    
