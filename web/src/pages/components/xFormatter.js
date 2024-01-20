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

/**
 * @param {string | number | Date} inputTime
 * @returns {string}
 */
export function formatTime(inputTime) {
  const date = new Date(inputTime);
  const monthNames = [
    'Januari', 'Februari', 'Maret',
    'April', 'Mei', 'Juni', 'Juli',
    'Agustus', 'September', 'Oktober',
    'November', 'Desember'
  ];

  const day = date.getDate();
  const monthIndex = date.getMonth();
  const year = date.getFullYear();
  let hh = date.getHours();
  // @ts-ignore
  if( hh<10 ) hh = '0' + hh;
  let mm = date.getMinutes();
  // @ts-ignore
  if( mm<10 ) mm = '0' + mm;

  const formattedDate = `${day} ${monthNames[monthIndex]} ${year}, pada ${hh}:${mm}`;
  return formattedDate;
}