window.onload = () => {
    const table = document.getElementById('sortable_table');
    const headers = table.querySelectorAll('th');

    const tableBody = table.querySelector('tbody');
    const rows = tableBody.querySelectorAll('tr');

    [].forEach.call(headers, (header, index) => {
        header.addEventListener('click', () => {
            sortColumn(index);
            console.log(header);
        });
    });

    const sortColumn = function (index) {
        const newRows = Array.from(rows);
        console.log(newRows);
        newRows.sort((rowA, rowB) => {
            const cellA = rowA.querySelectorAll('td')[index].innerHTML;
            const cellB = rowB.querySelectorAll('td')[index].innerHTML;

            if (cellA > cellB) {
                return 1;
            } else if (cellA < cellB) {
                return -1;
            } else {
                return 0;
            }
        });
        console.log(newRows);

        [].forEach.call(rows, row => {
            tableBody.removeChild(row);
        });

        newRows.forEach(row => {
            tableBody.appendChild(row);
        });
    };
};