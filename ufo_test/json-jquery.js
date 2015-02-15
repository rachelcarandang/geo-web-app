// var data = { "users" : [ 
// {
// "firstName" : "Ray" , "lastName" : "Jones"
// },
// {
// "firstName" : "R" , "lastName" : "C"
// },

// ]};
// //alert(data.users[0].firstName);

// var output = "<ul>";
// for (var user in data.users) {
//     output += "<li><i>" + data.users[user].firstName + "</i></li>";
// }
// output += "</ul>";

// document.getElementById("placeholder").innerHTML = output;


// $.getJSON('sightings.json', function(data) {
// }.error(function(xhr) {
//     alert(xhr)
// }
// );

// ///////////////////////////////////////////
// // SOMEHOW THIS WORKS /////////////////////
// ///////////////////////////////////////////
// $.ajax({                    
//     url: 'http://127.0.0.1:5000/sightings/',
//     type: 'POST',
//     data: {
// 	limit : 3,
//     },
//     dataType: 'jsonp',
//     cache: false,
//     success: function( data, status ){
//         alert('ajax success');
//         //alert(JSON.stringify(data));
// 	var str = JSON.stringify(data);
// 	document.getElementById("str").innerHTML = str + "end";
// 	var output = "<p></p>";
// 	for (i in data.items) {
// 	    output += "<p>" + data.items[i].location + "</p>";
// }
// 	document.getElementById("list").innerHTML = output;
//         //alert( data.responseData.results.length + ' results found!' );
//     },
//     error: function(xhr, textStatus, err) { //odstampaj textStatus, err jbt
//         alert('ajax error');
//         alert(textStatus);
//         alert(err);
//         alert("readyState: "+xhr.readyState+"\n xhrStatus: "+xhr.status);
//         alert("responseText: "+xhr.responseText);
//     }
// }); 


$(document).ready(function() {
    $('#submit_limit').click(function() {
	if ($('#limit').val().length==0) {
	    $('#clean_output').html('Need to enter a value');
	}
	else {
	    get_sightings();
	}
    }); // end submit_limit click function
}); // end document ready

function get_sightings() {

    var limit = $('#limit').val();
    var ur = 'http://127.0.0.1:5000/sightings/';
    $.ajax({                    
	url: ur,
	type: 'GET',
	data: {
	    limit : limit,
	},
	dataType: 'jsonp',
	cache: false,
	success: function( data, status ){
            //alert('get sightings ajax success, limit was ' + lim + JSON.stringify(data));
	    var str = JSON.stringify(data);
	    $('#raw_output').html(str)

	    var output = "<p></p>";
	    for (i in data.items) {
	    	output += "<p>" + data.items[i].location + "</p>";
	    }
	    $("#clean_output").html(output);

            //alert( data.responseData.results.length + ' results found!' );
	},
	error: function(xhr, textStatus, err) { //odstampaj textStatus, err jbt
	    // error
            // alert('get sightings ajax error');
	    // alert("lim was" + lim);
            // alert(textStatus);
            // alert(err);
            $('#errors').html("error: " + err + "\n textStatus" + textStatus + "\n lim was" + lim + "\n xhr readyState:" + xhr.readyState+ "\n xhrStatus: "+xhr.status + "\n responseText" + xhr.responseText);
            //alert("responseText: "+xhr.responseText);
	}
    }); 


}



/////////////////////////////////////////////
/////////////////////////////////////////////
/////////////////////////////////////////////


//document.getElementById("ufos").innerHTML = "testing";


// $(document).ready(function(){
//     //attach a jQuery live event to the button
//     $('#getdata-button').live('click', function(){
//         $.getJSON('json-data.php', function(data) {
//             //alert(data); //uncomment this for debug
//             //alert (data.item1+" "+data.item2+" "+data.item3); //further debug
//             $('#showdata').html("<p>item1="+data.item1+" item2="+data.item2+" item3="+data.item3+"</p>");
//         });
//     });
// });

// $(document).ready(function(){
//     $('#getdata-button').live('click', function(){
//         $.getJSON('/sightings', {}, function(data) {
//             $('#showdata').html("<p>item1="+data.item1+" item2="+data.item2+" item3="+data.item3+"</p>");
//         });
//     });
// });

// $.ajax({
// type: "GET",
// url: '/sightings',
// async: false,


 // $.getJSON("http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?",
 //      {
 //        tags: "mount rainier",
 //        tagmode: "any",
 //        format: "json"
 //      },
 //      function(data) {
 //        $.each(data.items, function(i,item){
 //          $("<img/>").text("hello world!");
 //          if ( i == 3 ) return false;
 //        });
 //      });


 // $.getJSON("/sightings",
 //      function(data) {
 // 	  var items = [];
 //        $.each(data, function(key,value){
 //          items.push( "<li id='" + key + "'>" + val + "</li>" );
 //        });
 //  $( "<ul/>", {
 //    "class": "my-new-list",
 //    html: items.join( "" )
 //  }).appendTo( "body" );
 //      });


// $.ajax({
// type: "POST",
// url: "/sightings",
// contentType: "application/json; charset=utf-8",
// dataType: "json",
// success: function (result) {
// var Mydata = result.d;
// //$("#dictionary").append(Mydata);
// $("p").text("Hello world!");
// }
// });
// });
// });
