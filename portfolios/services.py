from .models import UserInfo,Highlight,Section,SectionData
background_templates = {
        "bg0": "designs/default.html",
        "bg1": "designs/bg2.html",
        "bg2": "designs/bigbox.html",
        "bg3": "designs/checkboard.html",
        "bg4": "designs/dotted.html",
        "bg5": "designs/dottedbg.html",
        "bg6": "designs/graphbigboxes.html",
        "bg7": "designs/overlay.html",
        "bg8": "designs/test.html",
        "bg9": "animated/canvas.html",
        "bg10": "animated/circle.html",
        "bg11": "animated/colorcircle.html",
        "bg12": "animated/diagonalstrip.html",
        "bg13": "animated/hexagon.html",
        "bg14": "animated/polygon.html",
        "bg15": "animated/star.html",
        "bg16": "animated/test.html",
        "bg17": "animated/particles.html",
        "bg18": "designs/Wavyy.html",
        "bg19": "designs/polygon.html",
        "bg20": "designs/Celebration.html",
        }


def get_user_data(user_info):
    """
    Returns user data
    """
    highlights = Highlight.objects.filter(user=user_info.user)
    sections = Section.objects.filter(user=user_info.user)
    user_info.selected_template = background_templates.get(user_info.selected_background)
    return highlights, sections, user_info