import folium


def quick_map():
    olium_map = folium.Map(location=[41.88, -87.62],
                           zoom_start=13,
                           tiles="cartodbpositron",
                           width='75%',
                           height='75%')

    return {"msg": "ok"}
