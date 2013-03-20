$(document).keydown(function(e){ if (e.keyCode = (tab-key?)){
       $('input.autotab').trigger('tab:press');
   });

// takes a text field and an array of strings for autocompletion
$('input.autotab').bind('tab:press', function(){
   var userInput = $(inputField);
   var userlist = array("tom","dick","harry")// get array of current users
   autocomplete(userInput,userlist);
 });

function autocomplete(input, userlist) {
  var toComplete = text.slice(text.lastIndexOf(" ") + 1);

  if (toComplete.value.length == toComplete.selectionStart && toComplete.value.length == toComplete.selectionEnd) {
    var suggestionss = []
    for (var i=0; i < userlist.length; i++) {
      if (userlist[i].indexOf(toComplete.value) == 0 && userlist[i].length > toComplete.value.length)
        suggestionss.push(userlist[i])
    }

    if (suggestionss.length > 0) {
      if (suggestionss.length == 1) input.value = suggestionss[0]
      else toComplete.value = longestInCommon(suggestionss, toComplete.value.length)
      return true
    }
  }
  return false
}

function longestInCommon(suggestionss, index) {
  var i, ch, memo
  do {
    memo = null
    for (i=0; i < suggestionss.length; i++) {
      ch = suggestionss[i].charAt(index)
      if (!ch) break
      if (!memo) memo = ch
      else if (ch != memo) break
    }
  } while (i == suggestionss.length && ++index)

  return suggestionss[0].slice(0, index)
}
