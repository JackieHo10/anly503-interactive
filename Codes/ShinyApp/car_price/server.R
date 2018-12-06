#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#
data<-read.csv("cleaned_carscom.csv")
col_class<-sapply(data,class)
col_class[2]="character"
data<-read.csv("cleaned_carscom.csv",colClasses = col_class)
data[!data$bodyStyle %in% c("SUV","Sedan","Crew Cab Pickup","Coupe","Convertible"),"bodyStyle"]="Others"

library(shiny)
library(ggplot2)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
   
 
  output$value <- renderPlot({ 
    selection_1<-as.logical(data$certified) %in% c(input$check1)
   
    selection_2<-data$bodyStyle %in% c(input$check2)
    selection_3<-(data$year>=input$slider1[1]) & (data$year<=input$slider1[2])
    selection_4<-(data$mileage>=input$slider2[1]) & (data$mileage<=input$slider2[2])
    selection_index<-selection_1&selection_2&selection_3&selection_4
    
    price=data[selection_index,"price"]
    df=data.frame("price"=price)
    p  <- ggplot(df,aes(price))+
    geom_histogram(color="black", fill="#E69F00")+
    labs(title="Price Histogram",x="Price(US dollars)", y = "Frequency")+
      theme(plot.title = element_text(size=22))
    p
    
    })
  
})
