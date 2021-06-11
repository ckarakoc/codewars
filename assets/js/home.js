let table = document.getElementsByClassName('sortable')[0];
let thead = table.getElementsByTagName('thead')[0];
let tbody = table.getElementsByTagName('tbody')[0];

let tHeaders = thead.getElementsByTagName('th');
let tBodyRows = tbody.getElementsByTagName('tr');

let sortedIdx = -1


sortable = {
    init: function () {
        sortable.sortColumn(0);

        Array.prototype.forEach.call(tHeaders, (th, colIdx) => {
            th.addEventListener('click', () => {
                sortable.sortColumn(colIdx);
            });
        });
    },
    sortColumn: function (colIdx) {
        let clonedRows = Array.from(tBodyRows);
        if (sortedIdx === colIdx) {
            clonedRows.reverse();
            sortedIdx = -1;
        } else {
            clonedRows.sort((trA, trB) => {
                let cellA = trA.cells[colIdx].innerHTML
                let cellB = trB.cells[colIdx].innerHTML

                if (cellA > cellB) {
                    return 1;
                } else if (cellA < cellB) {
                    return -1;
                } else {
                    return 1
                }
            });
            sortedIdx = colIdx;
        }

        Array.prototype.forEach.call(tBodyRows, row => {
            tbody.removeChild(row);
        });

        clonedRows.forEach(row => {
            tbody.appendChild(row);
        });
    }
};

window.onload = sortable.init;
