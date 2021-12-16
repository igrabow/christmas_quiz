import yt_dlp as youtube_dl
import os


def download(name, link):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=link, download=False
    )
    filename = name
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'app/static/'+filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format('app/static/'+filename))


if __name__ == '__main__':
    videos = {
        "froehliche_weihnacht.mp3": "https://www.youtube.com/watch?v=FogVyl1Imnc",
        "ihr_kinderlein_kommet.mp3": "https://www.youtube.com/watch?v=vbxbytIPWmE",
        "kling_gloeckchen.mp3": "https://www.youtube.com/watch?v=Ebxa7oYNud0",
        "kommet_ihr_hirten.mp3": "https://www.youtube.com/watch?v=P4a3Cgg87ik",
        "leise_rieselt_der_schnee.mp3": "https://www.youtube.com/watch?v=m13xwWorw9s",
        "macht_hoch_die_tuer.mp3": "https://www.youtube.com/watch?v=iXpqoP4PLxg",
        "morgen_kinder_wirds_was_geben.mp3": "https://www.youtube.com/watch?v=fTWHUOCM2_Q",
        "o_du_froehliche.mp3": "https://www.youtube.com/watch?v=rJgeLuWEodQ",
        "o_tannenbaum.mp3": "https://www.youtube.com/watch?v=PamrmrVB5Mo",
        "schneefloeckchen.mp3": "https://www.youtube.com/watch?v=YXBkDH3hm_s",
        "suesser_die_glocken_nie_klingen.mp3": "https://www.youtube.com/watch?v=ciE9_FqjwNc",
        "stille_nacht_heilige_nacht.mp3": "https://www.youtube.com/watch?v=ohhXZtgO3J8",
        "jingle_bell_rock.mp3": "https://www.youtube.com/watch?v=Z0ajuTaHBtM",
        "santa_baby.mp3": "https://www.youtube.com/watch?v=StTJTJaoccY",
        "last_christmas.mp3": "https://www.youtube.com/watch?v=FuAHR4lkjCo",
        "driving_home_for_christmas.mp3": "https://www.youtube.com/watch?v=EvDxSW8mzvU",
        "santa_claus_is_coming_to_town.mp3": "https://www.youtube.com/watch?v=Vhv_47ghQuY",
        "rudolph_the_red_nosed_reindeer.mp3": "https://www.youtube.com/watch?v=ADAzftjx2tg",
        "wonderful_dream.mp3": "https://www.youtube.com/watch?v=gdjFeiiJaPI",
        "carol_of_the_bells.mp3": "https://www.youtube.com/watch?v=Uizt7qtAtA0",
        "white_christmas.mp3": "https://www.youtube.com/watch?v=30TkClWvT5k",
        "rockin_around_the_christmas_tree.mp3": "https://www.youtube.com/watch?v=dxHL36aJvGU",
        "santa_tell_me.mp3": "https://www.youtube.com/watch?v=jnXxxKZ57Tw",
        "its_beginning_to_look_a_lot_like_christmas.mp3": "https://www.youtube.com/watch?v=vUiHsJrRNGE",
        "in_der_weihnachtsbaeckerei.mp3": "https://www.youtube.com/watch?v=IFZqDcFU4Ow",



    }
    for name, link in videos.items():
        download(name, link)
