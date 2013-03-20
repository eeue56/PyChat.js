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
    var suggestions = []
    for (var i=0; i < userlist.length; i++) {
      if (userlist[i].indexOf(toComplete.value) == 0 && userlist[i].length > toComplete.value.length)
        suggestions.push(userlist[i])
    }

    if (suggestions.length > 0) {
      if (suggestions.length == 1) input.value = suggestions[0]
      else toComplete.value = longestInCommon(suggestions, toComplete.value.length)
      return true
    }
  }
  return false
}
function longestInCommon(suggestions, index) {
  var i, ch, memo
  do {
    memo = null
    for (i=0; i < suggestions.length; i++) {
      ch = suggestions[i].charAt(index)
      if (!ch) break
      if (!memo) memo = ch
      else if (ch != memo) break
    }
  } while (i == suggestions.length && ++index)

  return suggestions[0].slice(0, index)
}
