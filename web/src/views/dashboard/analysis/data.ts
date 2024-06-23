export interface GrowCardItem {
  icon: string;
  title: string;
  value: number;
  total: number;
  color: string;
  action: string;
}

export const growCardList: GrowCardItem[] = [
  {
    title: 'Количество посещений', // "访问数"  - "Количество посещений"  более  точный  и  понятный  перевод  в  русском  языке
    icon: 'visit-count|svg',
    value: 2000,
    total: 120000,
    color: 'green',
    action: 'Месяц', //  "月"  - "Месяц"  более  точный  перевод  в  русском  языке
  },
  {
    title: 'Сумма сделок', // "成交额" - "Сумма сделок"  более  точный  и  понятный  перевод  в  русском  языке
    icon: 'total-sales|svg',
    value: 20000,
    total: 500000,
    color: 'blue',
    action: 'Месяц', //  "月"  - "Месяц"  более  точный  перевод  в  русском  языке
  },
  {
    title: 'Количество загрузок', // "下载数" - "Количество загрузок"  более  точный  и  понятный  перевод  в  русском  языке
    icon: 'download-count|svg',
    value: 8000,
    total: 120000,
    color: 'orange',
    action: 'Неделя', //  "周" - "Неделя"  более  точный  перевод  в  русском  языке
  },
  {
    title: 'Количество сделок', // "成交数" - "Количество сделок"  более  точный  и  понятный  перевод  в  русском  языке
    icon: 'transaction|svg',
    value: 5000,
    total: 50000,
    color: 'purple',
    action: 'Год', // "年" - "Год"  более  точный  перевод  в  русском  языке
  },
];