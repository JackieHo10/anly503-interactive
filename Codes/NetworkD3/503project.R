# ANLY503 Final Project #
#Network D3
setwd("C:/Users/jacky/Desktop/HW/ANLY503/Project")
rm(list=ls())
#import library
library(igraph)
library(networkD3)
library(xlsx)
#load data
url <- "https://raw.githubusercontent.com/minfrdata/ANLY503Project1/master/code/Price_Volume/networks/net_id2.csv"
mydf <- read.csv(url(url), header = TRUE, sep = ",")
edgeList <- mydf[mydf$no > 10, ] #only keep large volumn
#save for future use
write.xlsx(edgeList, file = "SellerVSDealer.xlsx")
edgeList <- edgeList[, -c(1,4)]
brands <- unique(edgeList$make_)
#create a graph
gd <- igraph::simplify(igraph::graph.data.frame(edgeList, directed=FALSE))
#create node list
nodeList <- data.frame(ID = c(0:(igraph::vcount(gd) - 1)), nName = igraph::V(gd)$name)
getNodeID <- function(x){
  which(x == igraph::V(gd)$name) - 1
}
edgeList <- plyr::ddply(edgeList, .variables = c("seller", "make_", "no"), 
                        function (x) data.frame(SourceID = getNodeID(x$seller), 
                                                TargetID = getNodeID(x$make_)))
#calculate node degrees
nodeList <- cbind(nodeList, nodeDegree=igraph::degree(gd, v = igraph::V(gd), mode = "all"))
#calculate node betweenness
betAll <- igraph::betweenness(gd, v = igraph::V(gd), directed = FALSE) / (((igraph::vcount(gd) - 1) * (igraph::vcount(gd)-2)) / 2)
betAll.norm <- (betAll - min(betAll))/(max(betAll) - min(betAll))
nodeList <- cbind(nodeList, nodeBetweenness = 100*betAll.norm)
#calculate node dice similarities
dsAll <- igraph::similarity.dice(gd, vids = igraph::V(gd), mode = "all")
F1 <- function(x) {
  data.frame(diceSim = dsAll[x$SourceID + 1, x$TargetID + 1])
  }
edgeList <- plyr::ddply(edgeList, .variables=c("seller", "make_", "no", "SourceID", "TargetID"), function(x) data.frame(F1(x)))
#set color of edges
F2 <- colorRampPalette(c("#FFFF00", "#FF0000"), bias = nrow(edgeList), space = "rgb", interpolate = "linear")
colCodes <- F2(length(unique(edgeList$diceSim)))
edges_col <- sapply(edgeList$diceSim, function(x) colCodes[which(sort(unique(edgeList$diceSim)) == x)])
#create the network
D3_network <- networkD3::forceNetwork(Links = edgeList, 
                                         Nodes = nodeList, 
                                         Source = "SourceID", 
                                         Target = "TargetID", 
                                         Value = "no", 
                                         NodeID = "nName", 
                                         Nodesize = "nodeBetweenness",  
                                         Group = "nodeDegree", 
                                         height = 700, 
                                         width = 1200,  
                                         fontSize = 15, 
                                         linkDistance = networkD3::JS("function(d) { return 1*d.value; }"),
                                         linkWidth = networkD3::JS("function(d) { return d.value/50; }"),
                                         opacity = 0.5, 
                                         zoom = TRUE,
                                         opacityNoHover = 0.2,
                                         linkColour = edges_col) 
D3_network #plot
networkD3::saveNetwork(D3_network, "D3_R.html", selfcontained = TRUE) #save as html












