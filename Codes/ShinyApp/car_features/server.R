#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/

#
#setwd("C:/Users/nikhi/OneDrive/Documents/R/ShinyApp/car_features")

library(shiny)
#carfeatures<-data.frame("verify"=c())
verify<-c(0.08,0.92)
names(verify)<-c("verified","Non-verified")

cartype<-c(0.38,0.27,0.13,0.08,0.14)
names(cartype)<-c("SUV","Sedan","Crew cab pickup","Coupe","Others")

carage<-c(0.082,0.471,0.223,0.223)
names(carage)<-c("1-2years","3-5years","6-8years","8+years")

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
   
  output$distPlot <- renderPlot({
    # Create test data.
    if (input$select=="verify"){
      dat = data.frame(count=verify, category=names(verify))}
    if (input$select=="cartype"){
      dat = data.frame(count=cartype, category=names(cartype))}
    if (input$select=="carage"){
      dat = data.frame(count=carage, category=names(carage))}
    
    
    # Add addition columns, needed for drawing with geom_rect.
    dat$fraction = dat$count / sum(dat$count)
    dat = dat[order(dat$fraction), ]
    dat$ymax = cumsum(dat$fraction)
    dat$ymin = c(0, head(dat$ymax, n=-1))
    
    library(ggplot2)
    library(ggiraph)
    # pie
  
  
    pie<- ggplot(dat, aes(x=category, y=fraction))+
      geom_col(aes(fill = category))+
      #coord_polar("y", start=0)+
      ggtitle("Distribution of trade amont by selected features") +
      labs(x="Category",y="Percentage") + 
      scale_fill_brewer(palette="Blues")+
      theme_light()
    pie
   
    
  })
  
  output$value <- renderPrint({ input$select })
  
})




