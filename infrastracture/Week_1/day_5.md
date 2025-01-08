# Day 5

on this day i finish and completed all 
thing in [mind map](https://lucid.app/lucidspark/93e0901f-fd33-4817-af9c-0cc6ce533511/edit?viewport_loc=-1210%2C115%2C3276%2C1615%2C0_0&invitationId=inv_f2467779-a06e-4b60-9470-0347a8ab6ccf), specially i wroked in chat section and refactor the mind map.

I also search alot in the stories & reels section in the instgram and found this [article](https://freedium.cfd/https://blog.devgenius.io/system-design-instagram-reels-9707d7eba8ab) useful.

After some searching in the Stories section on instagram i reialize some things:

1. instagram build the media structure in the backend and save it in aws s3 then moved to fbcdn .

2. instagram frontend takes the video url of the story or the reals video and transform it into blob object and run this blob object in the video.

3. instagram transform the incoming videos url to blob for some reasons [ ChatGPT ]:
    1. **Security and Privacy**

        Content Protection: By converting video URLs into Blob URLs, Instagram can obscure the actual source of the video. This makes it harder for unauthorized users to directly download or share the content.
        Access Control: Blob URLs are created in the context of the user's session and are not easily accessible outside that context, which helps protect user-generated content.

    2. **Performance Optimization**

        Loading Efficiency: Blob URLs allow for more efficient loading of media. The video can be streamed in chunks, which reduces initial loading times and improves playback performance.
        Caching: Blob URLs can be cached in the browser's memory, allowing for faster access to recently viewed videos without needing to re-fetch them from the server.

    3. **Cross-Origin Resource Sharing (CORS)**

        Avoiding CORS Issues: Using Blob URLs can help mitigate CORS-related issues that arise when trying to request resources from different origins. By serving the media from a Blob URL, Instagram can control access more effectively.

    4. **User Experience**

        Seamless Playback: Blob URLs can provide a smoother user experience by allowing for immediate playback of videos without the need for full downloads.
        Adaptive Streaming: Instagram can implement adaptive bitrate streaming, where the quality of the video adjusts based on the user's connection speed, enhancing the viewing experience.

    5. **Data Management**

        Dynamic Content Serving: Blob URLs can be generated on-the-fly, allowing Instagram to serve different video versions based on various factors like user preferences, device capabilities, and network conditions.

    6. **Reduced Direct Linking**

        Preventing Direct Access: By converting URLs to Blob format, Instagram can reduce the likelihood of users directly linking to media files, which can lead to unauthorized sharing and distribution.
