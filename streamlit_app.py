import streamlit as st
import folium
from streamlit_folium import st_folium

LEGEND_URL = (
    "https://maps.geogratis.gc.ca/wms/elevation_en?"
    "version=1.3.0&service=WMS&request=GetLegendGraphic"
    "&sld_version=1.1.0&layer=cdem.color-shaded-relief"
    "&format=image/png&STYLE=default"
)


st.set_page_config(layout="wide")
st.title("Canadian Digital Elevation Model (CDEM) – Shaded Relief")

lat, lon = 54.13, -108.43

m = folium.Map(location=[lat, lon], zoom_start=8, control_scale=True)

folium.TileLayer('OpenStreetMap').add_to(m)

folium.raster_layers.WmsTileLayer(
    url="https://maps.geogratis.gc.ca/wms/elevation_en?",
    layers="cdem.color-shaded-relief",
    name="CDEM Color Shaded Relief",
    fmt="image/png",
    transparent=True,
    version="1.3.0",
    attr="Natural Resources Canada - GeoGratis",
    overlay=True,
    control=True,
).add_to(m)

folium.LayerControl().add_to(m)

col1, col2 = st.columns([12, 1])
with col1:
    st_folium(m, use_container_width=True, height=800)
with col2:
    st.markdown("### Legend")
    st.image(
        LEGEND_URL,
        caption="Elevation (m)",
        use_container_width=True
    )
