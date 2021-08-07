function sousin(){
    let usesrname = $("#wrapper>#contact>name").val();
    let email = $("#wrapper>#contact>email").val();
    let requirements = $("#wrapper>#contact>requirements").val();
    let Contents = $("#wrapper>#contact>Contents").val();

    Email.send({
        Host : "smtp.yourisp.com",
        Username : usesrname,
        To : 'airmac.baslove@gmail.com',
        From : email,
        Subject : requirements,
        Body : Contents
    }).then(
      message => alert(message)
    );
}
$(function(){
	$(".btn-gnavi").on("click", function(){
		var rightVal = 0;
		if($(this).hasClass("open")) {
			rightVal = -300;
			$(this).removeClass("open");
		} else {
			$(this).addClass("open");
		}
		$("#global-navi").stop().animate({
			right: rightVal
		}, 200);
	});
});