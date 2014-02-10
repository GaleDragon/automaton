$(function poll(){
    var finished = false;
    while (!finished) {
        $.ajax({
            type: "GET",
            url: "results/progress",
            data: { user_profile_id : "" }
        });
    }
});