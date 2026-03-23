### Query : 
             The role of query in parameters is as important the filter in any search , without it the api will not know that out of thousands of results which one to show.
### Reason of using the response.json() instead of response.text() :
                                        reason of using is that by using .json() we can access the keys of data in dictionary form . but by using the .text() , we will be having the data in string format , and hence not accessable in key , value format . 