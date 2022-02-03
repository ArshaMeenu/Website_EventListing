$(document).ready(function(){


// like 
           console.log("working set");
           $('.like-form').submit(function(e){
        e.preventDefault();
         const video_id=$('.like-btn').val();
         const token=$('input[name=csrfmiddlewaretoken]').val();
         const url=$(this).attr('action') 
       $.ajax({
           method:"POST",
           url:url,
           headers:{'X-CSRFToken': token},
           data:{
               'video_id':video_id
           },
           success:function(response){
            if(response.liked===true){
                       console.log("liked true");
                $('.like-icon').addClass('text-primary')
              }else{
                       console.log("liked false");

                $('.like-icon').removeClass('text-primary')
              }
            
               like=$('#like-count').text(response.likes_count)
               parseInt(like)
           },
           error:function(response){
            console.log("Failed ", response)
           }
       })
    })


           
    //dislike ajax call

    $('.dislike-form').submit(function(e){
           e.preventDefault()
          const event_id=$(".dislike-btn").val()
          const token=$('input[name=csrfmiddlewaretoken]').val() 
          const url =$(this).attr('action') 
             $.ajax({
                  method:"POST",
                  url:url,
                  headers:{"X-CSRFToken": token},
                  data:{
                      'event_id':event_id
                  },
                  success:function(response){
                      console.log(response)
                      if(response.disliked ===true){
                          $(".dislike-icon").addClass("text-primary")
                      }else{
                          $(".dislike-icon").removeClass("text-primary")
                      }
                  
                      dislikes=$("#dislike-count").text(response.dislike_count)
                      parseInt(dislikes)
                      
                  },
                  error:function(response){
                      console.log('failed', response)
                  }
              }) 
      
      })
   


});