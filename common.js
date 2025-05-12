$("#exportTransactionHistory").on("click", function () {
    // Select the transaction table and convert it to an array of data
    var table = $("table.table");
    var rows = table.find("tbody tr");

    var transactionData = [];
    rows.each(function () {
        var row = $(this);
        var rowData = [];
        row.find("td").each(function () {
            rowData.push($(this).text());
        });
        transactionData.push(rowData);
    });

    // Add header row (You can customize the column headers as needed)
    var header = ["Date", "Order Number", "Customer Name", "Total Cost"];
    transactionData.unshift(header);

    // Create a worksheet
    var ws = XLSX.utils.aoa_to_sheet(transactionData);

    // Create a workbook
    var wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Transactions");

    // Export the workbook to an Excel file
    XLSX.writeFile(wb, "transaction_history.xlsx");
});
