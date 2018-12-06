library(rgdal)
library(magrittr)
library(htmlwidgets)
library(leaflet)
library(sp)
library(mapproj)
library(maps)
library(mapdata)
library(maptools)
library(htmlwidgets)
library(magrittr)
library(XML)
library(plyr)
library(rgdal)
library(WDI)
library(raster)
library(noncensus)
library(stringr)
library(tidyr)
library(tigris)
library(rgeos)
library(ggplot2)
library(scales)

data <- read.csv('leaf.csv')
states <- readOGR("cb_2017_us_state_20m.shp",
                  layer = "cb_2017_us_state_20m", GDAL1_integer64_policy = TRUE)

# Remove Puerto Rico (72), Guam (66), Virgin Islands (78), American Samoa (60)
#  Mariana Islands (69), Micronesia (64), Marshall Islands (68), Palau (70), Minor Islands (74)
states<- states[!states$STUSPS %in% c("PR"),]

countmap <- merge(states, data, by=c("STUSPS"))

# Format popup data for leaflet map.
#popup_dat <- paste0("<strong>State: </strong>", countmap$STUSPS, 
#                    "<br><strong>Number of Used cars: </strong>", countmap$count)
labels <- sprintf(
  "<strong>State: </strong> %s<br/><strong>Number of Used cars: </strong> %g",
  countmap$STUSPS,countmap$count
) %>% lapply(htmltools::HTML)


# Format popup data for leaflet map.
popup_11 <- paste0("<strong>State: </strong>", 
                   data$STUSPS, 
                   "<br><strong>The most popular body style: </strong>", 
                   data$No1_Highest, 
                   "<br><strong>The second popular: </strong>", 
                   data$No2_Highest, 
                   "<br><strong>The third popular: </strong>", 
                   data$No3_Highest)

#pal <- colorQuantile("YlOrRd", NULL, n = 9)

bins <- c(0, 14000,28000,42000,56000,70000,84000,98000,112000,126000,140000)
pal <- colorBin("YlOrRd", domain = data$count, bins = bins)


icons <- awesomeIcons(
  icon = 'ios-close',
  iconColor="black",
  markerColor='blue',
  library = 'ion'
)

gmap <- leaflet(countmap) %>%
  # Base groups
  addTiles() %>%
  setView(lng = -115, lat = 50, zoom = 2) %>% 
  addPolygons(fillColor = ~pal(count), 
              fillOpacity = 1, 
              highlight = highlightOptions(
                color = "blue",
                opacity=1,
                weight=2,
                fillOpacity = 2,bringToFront = TRUE,sendToBack = TRUE),
              label=labels,
              labelOptions= labelOptions(direction = 'auto'),
              color = "#000000", 
              weight = 1,
              #popup =popup_dat,
              group = "Volume of Used Cars in the U.S"
              ) %>% 
 
  addAwesomeMarkers(data=data,lat=~lat, lng=~long,icon=icons,popup=popup_11,group="Top 3 Popular Body Style")%>%

# Layers control
addLayersControl(
  baseGroups = c("Volume of Used Cars in the U.S"),
  overlayGroups = c("Top 3 Popular Body Style"),
  options = layersControlOptions(collapsed = FALSE)
)%>% 

addLegend(pal = pal, values = ~count, opacity = 0.7, title = NULL,
          position = "bottomright")


gmap
saveWidget(gmap, 'US_used_cars_map.html', selfcontained = TRUE)

