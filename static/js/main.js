!function(a){"use strict";a(function(){var b=a(window),c=a(document.body);c.scrollspy({target:".sidebar"}),b.on("load",function(){c.scrollspy("refresh")}),a(".bs-docs-container [href=#]").click(function(a){a.preventDefault()}),setTimeout(function(){var b=a(".sidebar");b.affix({offset:{top:function(){var c=b.offset().top,d=parseInt(b.children(0).css("margin-top"),10),e=a(".bs-docs-nav").height();return this.top=c-e-d},bottom:function(){return this.bottom=a(".bs-docs-footer")}}})},100);})}(jQuery);

$(function(){
    // Start Variables
    var sea_service = $(".sea-service-button");
    // var d = new Date();
    // var month = d.getMonth()+1;
    // var day = d.getDate();
    // var date = ((''+month).length<2 ? '0' : '') + month + '/' +
    //     ((''+day).length<2 ? '0' : '') + day + '/' + d.getFullYear(); 
    var x = ''; 
    count = 0;
    var seaservice_count = 9;
    // counter for sea service incremental purposes
    var seaservice_counter = 9;
    var college_count = 0;
    var emergency_count = 0;

    // full name in the bottom most of the code
    var full_name = function(){
                      last_name = $("#id_last_name").val();
                      first_name = $("#id_first_name").val();
                      middle_name = $("#id_middle_name").val();
                      full_name = $("#full_name").val(first_name+' '+middle_name+' '+last_name);
                    };

    // auto title tooltip if text is typed
    var tooltip = function(){
                    val = $(this).val();
                    if(val == ''){
                      $(this).attr("title", "");
                      $(this).attr("data-original-title", "");
                    }else{
                      placeholder = $(this).attr("placeholder");
                      $(this).attr("title", placeholder);
                      $(this).attr("data-original-title", placeholder);
                    }
                  };

    // same address function
    var address = function(){
        permanent_unit = $("#permanent_unit").val();
        permanent_street = $("#permanent_street").val();
        permanent_baranggay = $("#permanent_baranggay").val();
        permanent_municipality = $("#permanent_municipality").val();
        permanent_zip = $("#permanent_zip").val();
        current_unit = $("#current_unit").val();
        current_street = $("#current_street").val();
        current_baranggay = $("#current_baranggay").val();
        current_municipality = $("#current_municipality").val();
        current_zip = $("#current_zip").val();
        if(permanent_street == current_street && 
            permanent_unit == current_unit && 
            permanent_baranggay == current_baranggay &&
            permanent_municipality == current_municipality && 
            permanent_zip == current_zip){
          $("#same_address").prop("checked", true);
        }else{
          $("#same_address").prop("checked", false);
        }
    };         

    // 50 words essay word count validation
    var essay = function(event){
      var _essay = document.getElementById('id_essay');
      try{
        essay = _essay.value.match(/\S+/g).length;
      }
      catch(err){
        return false;
      }
      if(essay < 50){
        _essay.setCustomValidity('Please answer the essay with a minimum of fifty words');
        
      }else{
        _essay.setCustomValidity('');
      }
      $('#display_count').text(essay);
    }
    var hp_kw_grt_dwt_validator = function(x){
      if(x.hasClass('hp')){
        ul = x.parent();
        setTimeout(function(){ ul.next("td").children("ul").remove(); ul.next("td").children("input").removeAttr('required'); }, 100);
      }else if(x.hasClass('kw')){
        ul2 = x.parent();
        setTimeout(function(){ ul2.prev("td").children("ul").remove(); ul2.next("td").children("input").removeAttr('required'); }, 100);
      }
      if(x.hasClass('grt')){
        ul3 = x.parent();
        setTimeout(function(){ ul3.next("td").children("ul").remove(); ul3.next("td").children("input").removeAttr('required'); }, 100);
      }else if(x.hasClass('dwt')){
        ul4 = x.parent();
        setTimeout(function(){ ul4.prev("td").children("ul").remove(); ul4.next("td").children("input").removeAttr('required'); }, 100);
      }
    }
    // End Variables

    $("input[name='source']").click(function(e){
      var label = '';
      var inputs = '';
      var text = e.currentTarget.nextSibling.data
      var text = text.trim();
      if($(this).is(':checked') && text != 'Seafarer Center'){
        $('.specific').remove();
        if(text == 'Advertisements'){
          label = '<label class="specific">:</label>';
          inputs = advertisements;
        }
        else if(text == 'Internet'){ 
          label = '<label class="specific">:</label>';
          inputs = internet;
        }else if(text == "Referred By"){
          label = '<label class="specific">:</label> ';
          inputs = referrer;
          $("#id_referred_by").prop("required", "true");
        }
        $(this).parent().append(label+inputs);
      }
      else{
        $('.specific').remove();
      }
    });
    $("#same_address").change(function(){
      if($(this).is(':checked')){
        unit = $("#permanent_unit").val();
        street = $("#permanent_street").val();
        barangay = $("#permanent_barangay").val();
        municipality = $("#permanent_municipality").val();
        zip = $("#permanent_zip").val();
      }else{
        unit = "";
        street = "";
        barangay = "";
        municipality = "";
        zip = "";
      }
      $("#current_unit").val(unit);
      $("#current_street").val(street);
      // $("#current_town").val(town);
      $("#current_barangay").val(barangay);
      $("#current_municipality").val(municipality);
      $("#current_zip").val(zip);
    });
    $("#id_civil_status").change(function(){
      val = $('option:selected', this).text();
      if(val == 'Single' || val == 'Civil Status'){
        $("#id_married_date").val("");
        $("#id_spouse_last_name").val("");
        $("#id_spouse_first_name").val("");
        $("#id_spouse_middle_name").val("");
        $("#id_birthdate").val("");
        $("#id_spouse_contact").val("");
        $("#id_married_date").prop("disabled", true);
        $("#id_spouse_last_name").prop("disabled", true);
        $("#id_spouse_first_name").prop("disabled", true);
        $("#id_spouse_middle_name").prop("disabled", true);
        $("#id_birthdate").prop("disabled", true);
        $("#id_spouse_contact").prop("disabled", true);
      }else if(val == 'Domestic Partner'){
        $("#id_married_date").val("");
        $("#id_spouse_last_name").attr("Placeholder", "Live-in's Maiden Last Name");
        $("#id_spouse_first_name").attr("Placeholder", "Live-in's First Name");
        $("#id_spouse_middle_name").attr("Placeholder", "Live-in's Maiden Middle Name");
        $("#id_birthdate").attr("Placeholder", "Live-in's birthday");
        $("#id_spouse_contact").attr("Placeholder", "Live-in's Contact No.");
        $("#id_married_date").prop("disabled", true);
        $("#id_spouse_last_name").prop("disabled", false);
        $("#id_spouse_first_name").prop("disabled", false);
        $("#id_spouse_middle_name").prop("disabled", false);
        $("#id_birthdate").prop("disabled", false);
        $("#id_spouse_contact").prop("disabled", false);
      }else{
        $("#id_spouse_last_name").attr("Placeholder", "Spouse's Maiden Last Name");
        $("#id_spouse_first_name").attr("Placeholder", "Spouse's First Name");
        $("#id_spouse_middle_name").attr("Placeholder", "Spouse's Maiden Middle Name");
        $("#id_birthdate").attr("Placeholder", "Spouse's birthday");
        $("#id_spouse_contact").attr("Placeholder", "Spouse's Contact No.");
        $("#id_married_date").prop("disabled", false);
        $("#id_spouse_last_name").prop("disabled", false);
        $("#id_spouse_first_name").prop("disabled", false);
        $("#id_spouse_middle_name").prop("disabled", false);
        $("#id_birthdate").prop("disabled", false);
        $("#id_spouse_contact").prop("disabled", false);
      }
    });

    $('table.sea-services').find('.date-left').each(function(){
      if($(this).val() != ''){
        $(this).prop("disabled", false);
      }
    });


  // START College Dynamic Fields Scripts
    // undisplays all except the first college
    $(".colleges:not(:eq(0))").hide();
    // Makes sure the form group shows if fields are not null upon post request
    $(".colleges").each(function(){
      $(this).find('input').each(function(){
        val = $(this).val()
        if(val != ''){
          $(this).parent().parent().show();
        } 
      });
      if($(this).is(":visible")){
        college_count++;
        // alert(college_count);
      }
    });
    college_count--;
    if(college_count > 0){
      $(".delete-college").show();
    }
    // alert($(".colleges").eq(0).is(":visible"));
    $(".add-college").click(function(){
      college_count++;
      // alert(college_count);
      $(".delete-college").show();
      $(".colleges").eq(college_count).show();
      // alert($(".colleges").eq(college_count).show());
    });
    $("body").on("click", ".delete-college", function(){
      $(".colleges").eq(college_count).hide();
      $(".colleges").eq(college_count).find('input').val('');
      college_count--;
      if(college_count == 0){
        $(this).hide();
      }
    });
  // END College Dynamic Fields Scripts

  // START Emergency Contact Dynamic Fields Scripts
    $(".emergency-contacts:not(:eq(0))").hide();
    // Makes sure the form group shows if fields are not null upon post request
    $(".emergency-contacts").each(function(){
      $(this).children().children().find('input').each(function(){
        val = $(this).val();
        if(val != ''){
          $(this).parent().parent().parent().show();
        } 
      })
      if($(this).is(":visible")){
        emergency_count++;
      }
    });
    emergency_count--;
    if(emergency_count > 0){
      $(".delete-emergency").show();
    }
    $(".add-emergency").click(function(){
      emergency_count++;
      $(".delete-emergency").show();
      $(".emergency-contacts").eq(emergency_count).show();
    });
    $("body").on("click", ".delete-emergency", function(){
      $(".emergency-contacts").eq(emergency_count).hide();
      $(".emergency-contacts").eq(emergency_count).find('input').val('');
      emergency_count--;
      if(emergency_count == 0){
        $(this).hide();
      }
    });
  // END Emergency Contact Dynamic Fields Scripts

  
  // START Sea Service Dynamic Fields Scripts
    // Makes sure the form group shows if fields are not null upon post request
    $(".sea-service-row").each(function(){
      $(this).children().find("input").each(function(){
        val = $(this).val();
        if(val != ''){
          $(this).parent().parent().show();
        }
      });
    });
    $(".add-sea-service-row").click(function(){
      if(seaservice_count > 9){
        seaservice_counter++;
      }
      $(".sea-service-row").each(function(){
        if($(this).is(":visible")){
          seaservice_count++;
        }
      });
      seaservice_count-=seaservice_counter;
      $(".sea-service-row").eq(seaservice_count).show();
    });
  // END Sea Service Dynamic Fields Scripts

    $("input").change(function(){
      name = $(this).attr("name");
      val = $(this).val();
      if( name == "visa_application" || name == "detained" || name == "disciplinary_action" || name == "charged_offense" || name == "termination" ){
        if(val == 1){
          $(this).parent().parent().after("<textarea class='form-control' name='"+name+"_reason' placeholder='Write your reason here' required></textarea>")
        }else{
          $("textarea[name='"+name+"_reason']").remove();
        }
      }
      if( name == "us_visa" || name == "schengen_visa" ){
        if(val == 0){
          $("input[name='"+name+"_expiry']").prop("disabled", true);
          $("input[name='"+name+"_expiry']").val("");
        }else{
          $("input[name='"+name+"_expiry']").prop("disabled", false);
        }
      }
    });

    $("body").on("focus", ".date", function(){
      $(this).datepicker({ 
        changeYear: true, 
        changeMonth: true, 
        yearRange: "1950:+50", 
        showButtonPanel: true,
        closeText: 'Clear',
        beforeShow: function (e, t) {
          $("#ui-datepicker-div").addClass('HideTodayButton');
          if($(this).hasClass('birth_date')){
            $(this).datepicker("option", "maxDate", 0);
          }
        },
        onClose: function () {
          var event = arguments.callee.caller.caller.arguments[0];
          if ($(event.delegateTarget).hasClass('ui-datepicker-close')) {
            $(this).val('');
          }
          if($(this).hasClass('birth_date')){
            val = $(this).val();
            // alert('val');
            if(val != ''){
              var birthday = new Date(val);
              var today = new Date();
              var age = ((today - birthday) / (31557600000));
              var age = Math.floor( age );
            }else{
              var age = ''
            }
            $(".age").val(age);
          }
          if($(this).hasClass('date-joined') || $(this).hasClass('date-left')){
            val = $(this).val();
            date_val = new Date(val);
            // val2 is used to get the day after the day selected 
            val2 = new Date();
            val2.setDate(date_val.getDate() + 1);
            duration = $(this).parent().siblings("td").find(".duration");
            if($(this).hasClass('date-joined')){
              _date_left = $(this).parent().next("td").children();
              date_left = new Date(_date_left.val());
              if(val == ''){
                _date_left.prop("disabled", true);
              }else{
                _date_left.prop("disabled", false);
                setTimeout(function(){ _date_left.focus(); }, 1000);
                setTimeout(function(){ $(this).datepicker("show"); }, 1000);
              }
              // _date_left.datepicker({ minDate: val2   });
              // var minDate = _date_left.datepicker( "option", "minDate");
              // _date_left.datepicker("option", "minDate", val2);
              _date_left.val("");
              duration.val("");
            }else if($(this).hasClass('date-left')){
              date_joined = $(this).parent().prev("td").children().val();
              date_joined = new Date(date_joined);
              
              if( date_joined != '' ){
                total_duration = Math.abs(date_joined.getTime() - date_val.getTime());
                total_duration = Math.ceil(total_duration / (1000 * 3600 * 24));
              }
              if( total_duration ){
                duration.val(total_duration);
              }
            }
          }
        }
      });
    }).on("keydown", ".date", function(e){
      // prevents erasing via backspace
      if (e.which === 8) {
            e.preventDefault();
      }
    });
    $('.sidebar').on('activate.bs.scrollspy', function () {
      // boolean is used for the sea-service to pop-up only from top to bottom
      if ($(this).find("li.active").text().trim() == 'Emergency Contact Details'){
        x = 1;
      }if($(this).find("li.active").text().trim() == 'Background Information'){
        x = 0;
      }
      if ($(this).find("li.active").text().trim() == 'Sea Service' && x == 1){
        $(sea_service).click();
      }
      position_applied = $("#id_position_applied option:selected").text();
      alternative_position = $("#id_alternative_position option:selected").text();
      if(position_applied != "Engine Cadet" && position_applied != "Deck Cadet" && alternative_position != "Engine Cadet" && alternative_position != "Deck Cadet"){
        $("#application-form-essay").hide();
        $("#id_essay").removeAttr('required');
      }
    });
    $.fn.modal.Constructor.prototype.enforceFocus = function () { };

    $(".month-only").datepicker({ 
      showButtonPanel: true,
      changeYear: true,
      changeMonth: true,  
      dateFormat: 'M yy',
      beforeShow: function (e, t) {
        $("#ui-datepicker-div").addClass("hide-calendar");
        $("#ui-datepicker-div").addClass('HideTodayButton');
      },
      onClose: function(dateText, inst){
        // var n = Math.abs($("#ui-datepicker-div .ui-datepicker-month :selected").val() - 1) + 2;
        var month = $("#ui-datepicker-div .ui-datepicker-month :selected").val();
        var year = $("#ui-datepicker-div .ui-datepicker-year :selected").val();
        $(this).datepicker('setDate', new Date(year, month, 1));
        setTimeout(function(){ $("#ui-datepicker-div").removeClass("hide-calendar"); }, 300);
        setTimeout(function(){ $("#ui-datepicker-div").removeClass('HideTodayButton'); }, 300);
      }
    });

    // $('.application-date').val(date);
    $('[data-toggle="tooltip"]').tooltip({ html: true });
    $("input").keyup(tooltip).click(tooltip).focusout(tooltip);
    $("#id_last_name, #id_first_name, #id_middle_name").keyup(full_name).click(full_name).focusout(full_name);
    $("#permanent_unit, #current_unit, #permanent_street, #permanent_baranggay, #permanent_municipality, #permanent_zip, #current_street, #current_baranggay, #current_municipality, #current_zip").keyup(address).change(address);
    $(".essay").keyup(essay).click(essay).focusout(essay);
    // Used for sea-services validation
    // Users can not exit the sea-service unless valid
    $(".sea-services").on("keyup", "input", function(){
      $(this).parent().siblings().children().prop("required", "true");
    }).on("change", "select", function(){
      $(this).parent().siblings().children().prop("required", "true");
    });

    // $(".sea-services input").keyup(function(){
    //   $(this).parent().siblings().children().prop("required", "true");
      // $(this).parent().siblings("td:nth-child(2)").html("<button type='button' class='btn btn-warning clear-row'>Clear Row</button>");
    // });

    // Start Sea Service Validation
    $("#proceed-sea-service").click(function(){
      count = 0
      $('.sea-services').find('input').each(function(){
        x = $(this);
        if($(this).prop('required') && $(this).next('ul').length != 1 && $(this).val().length < 1){
          $(this).after("<ul class='errorlist'><li>This field is required.</li></ul>");
        }else if($(this).val().length >= 1 && $(this).next('ul').length == 1){
          // count--;
          x.next('ul').remove();
          hp_kw_grt_dwt_validator(x);
        }
        else if($(this).val().length >= 1 && $(this).next('ul').length == 0){
          hp_kw_grt_dwt_validator(x);
        }else if(!$(this).prop('required')){
          // alert('dean');
          // count--;
          $(this).next('ul').remove();
        }
      });
      $('.sea-services').find('select').each(function(){
        if($(this).prop('required') && $(this).next('ul').length != 1 && $('option:selected', this).text() == "Cause of Discharge"){
          // count++;
          $(this).after("<ul class='errorlist'><li>This field is required.</li></ul>");
        }else if($('option:selected', this).text() != "Cause of Discharge" && $(this).next('ul').length == 1){
          // count--;
          $(this).next('ul').remove();
        }
      });
      setTimeout(function(){ 
        // alert(count);
        $('.sea-services').find('ul.errorlist').each(function(){
          count++;
        });
        if(count == 0){ 
          // closes the modal 
          $('#seaservice').modal('hide');
          $('h5.validations').text("");
        }else{
          $('h5.validations').text(count+ " REQUIRED FIELDS NEED TO BE FILLED UP");
        } 
      }, 500);
    });

    $(".sea-services").on("keyup", ".hp", function(){
      val = $(this).val();
      kw = val * .746;
      kw = Math.round( kw * 10 ) / 10;
      $(this).parent().next("td").children().val(kw);
      $(this).parent().next("td").children().prop("required", false);
    });
    $(".sea-services").on("keyup", ".kw", function(){
      val = $(this).val();
      hp = val * 1.340;
      hp = Math.round( hp * 10 ) / 10;
      $(this).parent().prev("td").children().val(hp);
      $(this).parent().prev("td").children().prop("required", false);
    });
    // End Sea Service Validation

    $(".essay").trigger('click');
    $("#id_civil_status").trigger("change");
    // $(".cause_of_discharge").trigger("change");
    $("#application-form input").trigger("keyup");
    $("#application-form input[name='us_visa'], #application-form input[name='schengen_visa'], #id_civil_status").trigger("change");
    $("body").on("change", "select", function(){
      val = $(this).val();
      $(this).css("color", "#000");
    });
    $(".sea-services").on("click", ".clear-row", function(){
      count = 0;
      $(this).parent().siblings().children("input").val("");
      $(this).parent().siblings().children("select").val("Cause of Discharge");
      $(this).parent().siblings().children("select").css("color", "#c4c1c7");
      $(this).parent().siblings().children().removeAttr('required');
      $(this).parent().siblings().children("ul").remove();
      // $(this).remove();
      setTimeout(function(){ 
        $('.sea-services').find('ul.errorlist').each(function(){
            count++;
        });
        if( count > 0){
          $('h5.validations').text(count+ " REQUIRED FIELDS NEED TO BE FILLED UP");
        }else{
          $('h5.validations').text("");
        }
      }, 500);
    });

    // Enables the signature on the modal
    $('#signature').on('show.bs.modal', function (e){
      $(".jSignature").jSignature();
      $(".jSignature").resize();
    });

    $(".search-zip").click(function(){
      params = $(this).attr('data-params');
      barangay = $("#"+params+"_barangay").val();
      municipality = $("#"+params+"_municipality").val();
      address = barangay+"+"+municipality+"+"+"zip code";
      address = address.replace(/ /g,"+");
      var myWindow = window.open("http://www.google.com.ph/#q="+address, "", "width=1000, height=700");
    });
    $("body").on("click", ".emergency-search-zip", function(){
      params = $(this).attr('data-params')-1;
      barangay = $("#id_form-"+params+"-emergency_barangay").val();
      municipality = $("#id_form-"+params+"-emergency_municipality").val();
      address = barangay+"+"+municipality+"+"+"zip code";
      address = address.replace(/ /g,"+");
      var myWindow = window.open("http://www.google.com.ph/#q="+address, "", "width=1000, height=700");
    });
    
    if($("#id_alternative_position").val() != "Alternative Position"){
      $("#id_alternative_position").css("color", "#000");
    }
    if($("#id_position_applied").val() != "Position Applied"){
      $("#id_position_applied").css("color", "#000");
    }

    $("#id_alternative_position, #id_position_applied").change(function(){
      x = $('option:selected', this).text();
      if( x == 'Deck Cadet' || x == 'Engine Cadet' ){
        $("#application-form-essay").show();
        $("#id_essay").prop("required", "true");
      }
    });

    // Start Input Validations
    $("body").on("keydown", "input[type='number']", function(e){
      // Allow: backspace, delete, tab, escape, enter and .
      if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
           // Allow: Ctrl+A, Command+A
          (e.keyCode == 65 && ( e.ctrlKey === true || e.metaKey === true ) ) || 
           // Allow: home, end, left, right, down, up
          (e.keyCode >= 35 && e.keyCode <= 40)) {
               // let it happen, don't do anything
               return;
      }
      // Ensure that it is a number and stop the keypress
      if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
          e.preventDefault();
      }
    });
    // Prevents Enter
    $(".bs-docs-section").on("keydown", "input", function(e){
      if (e.which === 13) {
        e.preventDefault();
      }
    });
    // End Input Validations
    $("input[name='source']").each(function(){
      if($(this).is(':checked')){
        $(this).trigger("click");
      }
    });
}); 

// Start Webcam Scripts
webcam.set_api_url( '/application-form/tmp-image/?first' );
webcam.set_quality( 90 ); // JPEG quality (1 - 100)
webcam.set_shutter_sound( true ); // play shutter click sound
$(".webcam-container").html(webcam.get_html(220, 180));
webcam.set_hook( 'onComplete', 'my_completion_handler' );
  
function take_snapshot() {
  webcam.snap();
}

function my_completion_handler(msg) {
  d = new Date();
  if (msg != 'No data') {
    var image_url = msg;
    // show JPEG image in page
    // Extra parameter for Image Caching
    document.getElementById('picture-container').innerHTML = '<img src="' + image_url + '?'+d.getTime()+'"><input type="text" name="application_picture" value="'+image_url+'" style="display:none">';
    // reset camera for another shot
    webcam.reset();
    // $("#update_image").val("image");
  }
  else{
    alert("Python Error: " + msg);
  } 
}
// End Webcam Scripts