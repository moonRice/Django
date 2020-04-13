from django.shortcuts import render
from django.views.generic import View
from .models import SongInfo, iFrameM
from apps.music_apps.user_history.models import UserTypeHistory

# Create your views here.
from ..sing.models import SingerName, Zhuangji


def songsList(request, zhuanji_id):
    # （歌手介绍页面用于跳转到专辑、音乐列表页面）专辑的ID传进来（用于在音乐列表页首位放置专辑图片）

    singer_id = request.GET.get('singer_id')
    # 歌手的ID传进来（用于音乐列表页面的对应歌手所有专辑的展示）
    # 歌手ID暂时不做处理，无用

    try:
        # 歌曲列表的查询
        songs_list = SongInfo.objects.filter(song_list_id=int(zhuanji_id))
        if songs_list:
            for img in songs_list:
                try:
                    zhuanji_img = Zhuangji.objects.get(auth_id=singer_id, id=img.song_list_id)
                except Zhuangji.DoesNotExist:
                    return render(request, '404.html', {
                        'errmsg': '你又瞎填歌手ID了哟！别以为我不知道！！！！'
                    })
                st = SongInfo.objects.get(id=int(img.id))
                type = st.song_type.all()
        else:
            return render(request, '404.html', {
                'errmsg': '对不起，该专辑未收录任何歌曲！请联系站点管理员，蟹蟹~【难道说是你瞎填的专辑ID？】'
            })
    except SongInfo.DoesNotExist:
        return render(request, '404.html')
    contexr = {
        'songs_list': songs_list,
        'zhuanji_img': zhuanji_img,
        'type': type,
    }
    return render(request, 'music/demo/songs_list.html', contexr)


def SongsDetails(request, song_id):
    flag = True
    try:
        sty = SongInfo.objects.get(id=int(song_id))
        try:
            iF = iFrameM.objects.get(song_id=song_id)
        except iFrameM.DoesNotExist:
            return render(request, '404.html', {
                'errmsg': '对不起，音频资源未收录，请添加！'
            })
        types = sty.song_type.all()
    except SongInfo.DoesNotExist:
        flag = False
    if flag:
        sty = SongInfo.objects.get(id=int(song_id))
        iF = iFrameM.objects.get(song_id=song_id)
        types = sty.song_type.all()
        context = {
            's_i': sty,
            'type': types,
            'if': iF,
        }
        return render(request, 'music/demo/songs_info.html', context)
    else:
        return render(request, '404.html', {
            'errmsg': '小伙子，你想玩套路？你以为我不晓得你瞎填的歌曲ID~！'
        })