var main = function () {
    
    $('.fullform').hide();
    $('.comments').hide();
    $('.postcomment').hide();
    
    $(".friends-button").click(
        function(){
            
            $('.menu').animate({
                right: "0px"
            }, 300);
        
            
            $('body').animate({
                right: "250px"
            }, 300);
        }
    );
    
    $(".close").click(
        function(){
            
            $('.menu').animate({
                right: "-250px"
            }, 300);
        
            
            $('body').animate({
                right: "0px"
            }, 300);
        }
    );
    
    $(".startwriting").click(
        function(){
            
            $('.startwriting').hide(300);
            $('.fullform').show(300);
        }
    );
    
    $(".showcomments").click(
        function(){
            
            $('.comments').toggle(300);
        }
    );
    
    $(".startcomment").click(
        function(){
            
            $('.postcomment').show(300);
            $('.comments').show(300);
        }
    );
    
}

$(document).ready(main);