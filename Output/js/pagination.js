
$(document).ready(function() {
    $('#tablepagination').DataTable({"bInfo" : false,  "lengthChange": true, "dom": '<"top"f>rt<"bottom"p><"clear">', "order": [[ 1, "desc" ]]});
} );

$(document).ready(function() {
    $('#tablepagination2').DataTable({"bInfo" : false,  "lengthChange": true, "dom": '<"top"f>rt<"bottom"p><"clear">', "order": [[ 1, "desc" ]]});
} );

$(document).ready(function() {
    $('#tablepagination3').DataTable({"bInfo" : false,  "lengthChange": true, "dom": '<"top"f>rt<"bottom"p><"clear">', "order": [[ 1, "desc" ]]});
} );

window.onresize = function()
{
  map = document.getElementsByTagName('DivMappa')
  setTimeout( function() { map.updateSize();}, 200);
}