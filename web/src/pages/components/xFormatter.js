/**
 * @param {string | number | Date} inputDate
 * @returns {string}
 */
export function formatDate(inputDate) {
  const date = new Date(inputDate);
  const monthNames = [
    'Januari', 'Februari', 'Maret',
    'April', 'Mei', 'Juni', 'Juli',
    'Agustus', 'September', 'Oktober',
    'November', 'Desember'
  ];

  const day = date.getDate();
  const monthIndex = date.getMonth();
  const year = date.getFullYear();

  const formattedDate = `${day} ${monthNames[monthIndex]} ${year}`;

  return formattedDate;
}