function initPage(scope,data,currentPage,pageSize){
        scope.pageArray=[];

        scope.pageCount = parseInt((data.count-1)/pageSize+1);
        count = scope.pageCount;
        if(count<= 5){
           for(i=0 ; i<count;i++){
                var page={};
                page.num=i+1;
                scope.pageArray.push(page);
           }
        }else{
            if(currentPage>=5){
                scope.pageArray.push({num:1});
                scope.pageArray.push({num:'...',disabled:true});
                var forCount = currentPage+1;
                var start = currentPage - 2;
                if(currentPage+2>=count){
                    forCount = count;
                    start -= 1;

                }
                for(i=start;i<forCount;i++){
                    var page={};
                    page.num=i+1;
                    scope.pageArray.push(page);
                }
                if(forCount != count){
                    scope.pageArray.push({num:'...',disabled:true});
                    scope.pageArray.push({num:count});
                }

            }else{
                for(i=0;i<5;i++){
                    var page={};
                    page.num=i+1;
                    scope.pageArray.push(page);
                }
                scope.pageArray.push({num:'...',disabled:true});
                scope.pageArray.push({num:count});
            }
        }
        scope.currentPage  = currentPage;
        scope.nextPage = data.next;
        scope.previousPage = data.previous;


}

