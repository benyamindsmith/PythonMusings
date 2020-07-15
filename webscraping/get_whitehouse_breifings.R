library(rvest)

get_whitehouse_breifings<- function(){
  #Preliminary Functions
  
 
  
  
  pipeit<-function(url,code){
    read_html(url)%>%html_nodes(code)%>%html_text()
  }
  
  pipelink<-function(url,code){
    read_html(url)%>%html_nodes(code)%>%html_attr("href")
  }
  
  
  first_link<-"https://www.whitehouse.gov/briefings-statements/"
  
  # Get total number of pages
  
  pages<-pipeit(first_link,".page-numbers")
  
  pages<-as.numeric(pages[length(pages)])
  
  #Get all links
  all_pages<-c()
  
  for (i in 1:pages){
    all_pages[i]<-paste0(first_link,"page/",i,"/")
  }
  
  

  urls<-unname(sapply(all_pages,function(x){
        pipelink(x,".briefing-statement__title a")
        })) %>% unlist()
  
  breifing_content<-unname(sapply(all_pages,function(x){
    pipeit(x,".briefing-statement__content")
  })) %>%  unlist()

  
  # Data Wrangling
  
  test<-unname(sapply(breifing_content,function(x) gsub("\\n|\\t","_",x)))
  
  test<-unname(sapply(test,function(x) strsplit(x,"_")))
  
  test<-unname(sapply(test,function(x) x[x!=""]))
  
  breifing_type<-unname(sapply(test,function(x) x[1])) %>% unlist()
  title<-unname(sapply(test,function(x) x[2])) %>% unlist()
  dat<-unname(sapply(test,function(x) x[length(x)])) %>% unlist()
  category<-unname(sapply(test,function(x) if(length(x)>3){
    x[3]
  }else{
    "NA"
  })) %>% unlist()
  
  
  dt<- data.frame("Date"=dat,"Title"=title,"URL"=urls,"Issue Type"= breifing_type, "Category"=category)

  dt
}
