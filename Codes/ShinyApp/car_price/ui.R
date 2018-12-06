#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Dynamic Customized Car Price Distribution"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      checkboxGroupInput("check1", label = h4("Verified Cars"), 
                         choices = list("Verified" =T , "Not Verified" = F),
                         selected = F),
      
      checkboxGroupInput("check2", label = h4("Car type"), 
                         choices = list("SUV" ="SUV" , "Sedan" ="Sedan", "Crew Cab Pickup" ="Crew Cab Pickup","Coupe"="Coupe","Convertible"="Convertible","Others"="Others"),
                         selected = "SUV"),
      
    #   selectInput("select", label = h4("Brand"), 
     #              choices = list("Choice 1" = 1, "Choice 2" = 2, "Choice 3" = 3), 
      #             selected = 1),
      sliderInput("slider1", label = h4("Year"), min =1985, 
                  max = 2019, value = c(2010, 2018)),
       sliderInput("slider2", label = h4("Mileage Range"), min = 0, 
                   max = 149999, value = c(0, 40000))
    ),
    
    
    # Show a plot of the generated distribution
    mainPanel(
       plotOutput("value")
    )
  )
))
