$(document).ready(function() {
miDataTable();
} );




function  miDataTable(){
    $('#miTabla').DataTable({

      "language": {
      "emptyTable":			"<i>No hay datos disponibles en la tabla.</i>",
      "info":		   		"Start _START_ End _END_ Total _TOTAL_ ",
      "infoEmpty":			"Mostrando 0 registros de un total de 0.",
      "infoFiltered":			"(filtrados de un total de _MAX_ registros)",
      "infoPostFix":			"(Updated)",
      "lengthMenu":			"Show _MENU_ Records",
      "loadingRecords":		"Loading...",
      "processing":			"Processing...",
      "search":			"<span style='font-size:15px;'>Search:</span>",
      "searchPlaceholder":		"Search",
      "zeroRecords":			"No matches found.",
      "paginate": {
        "first":			"First",
        "last":				"Last",
        "next":				"Next",
        "previous":			"Previous"
      },
      "aria": {
        "sortAscending":	"Ordenación ascendente",
        "sortDescending":	"Ordenación descendente"
      }
    },

    "lengthMenu":		[[3,5,7, 10, 20, 25, 50, -1], [3,5,7, 10, 20, 25, 50, "All"]],
    "iDisplayLength":	3,





    });
}
