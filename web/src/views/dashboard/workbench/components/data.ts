interface GroupItem {
  title: string;
  icon: string;
  color: string;
  desc: string;
  date: string;
  group: string; // группа
}

interface NavItem {
  title: string;
  icon: string;
  color: string;
}

interface DynamicInfoItem {
  avatar: string;
  name: string;
  date: string;
  desc: string;
}

export const navItems: NavItem[] = [
  {
    title: 'Главная', // "首页" -  хороший вариант, но "Главная"  более  распространенный  и  понятный  для  русского  языка
    icon: 'ion:home-outline',
    color: '#1fdaca',
  },
  {
    title: 'Панель мониторинга', // "仪表盘"  -  более  точная  передача  смысла, но  "Панель мониторинга"  более  распространен  в  русском  языке 
    icon: 'ion:grid-outline',
    color: '#bf0c2c',
  },
  {
    title: 'Компоненты', // "组件"  -  хороший вариант, но  "Компоненты"  более  распространен  в  русском  языке 
    icon: 'ion:layers-outline',
    color: '#e18525',
  },
  {
    title: 'Администрирование системы', // "系统管理"  -  хороший  вариант, но  "Администрирование системы"  более  распространен  в  русском  языке
    icon: 'ion:settings-outline',
    color: '#3fb27f',
  },
  {
    title: 'Управление доступом', // "权限管理"  -  хороший вариант, но  "Управление доступом"  более  распространен  в  русском  языке 
    icon: 'ion:key-outline',
    color: '#4daf1bc9',
  },
  {
    title: 'Диаграммы', // "图表"  -  хороший вариант, но  "Диаграммы"  более  распространен  в  русском  языке
    icon: 'ion:bar-chart-outline',
    color: '#00d8ff',
  },
];

export const dynamicInfoItems: DynamicInfoItem[] = [
  {
    avatar: 'dynamic-avatar-1|svg',
    name: 'Вильям',
    date: 'Только что', // "刚刚"  -  хороший вариант, но  "Только что"  более  распространен  в  русском  языке 
    desc: `В <a>开源组</a> создал проект <a>Vue</a>`,
  },
  {
    avatar: 'dynamic-avatar-2|svg',
    name: 'Эйвен', //  "艾文" -  нужно  уточнить  правильный  перевод
    date: '1 час назад',
    desc: `Подписался на <a>Вильяма</a> `,
  },
  {
    avatar: 'dynamic-avatar-3|svg',
    name: 'Крис',
    date: '1 день назад',
    desc: `Опубликовал <a>личную запись</a> `,
  },
  {
    avatar: 'dynamic-avatar-4|svg',
    name: 'Fu',
    date: '2 дня назад',
    desc: `Опубликовал статью <a>Как написать плагин Vite</a> `,
  },
  {
    avatar: 'dynamic-avatar-5|svg',
    name: 'Пит',
    date: '3 дня назад',
    desc: `Ответил на вопрос <a>Джека</a> <a>Как оптимизировать проект?</a>`,
  },
  {
    avatar: 'dynamic-avatar-6|svg',
    name: 'Джек',
    date: '1 неделю назад',
    desc: `Закрыл вопрос <a>Как запустить проект</a> `,
  },
  {
    avatar: 'dynamic-avatar-1|svg',
    name: 'Вильям',
    date: '1 неделю назад',
    desc: `Опубликовал <a>личную запись</a> `,
  },
  {
    avatar: 'dynamic-avatar-1|svg',
    name: 'Вильям',
    date: '2021-04-01 20:00',
    desc: `Отправил код в <a>Github</a>`,
  },
];

export const groupItems: GroupItem[] = [
  {
    title: 'Github',
    icon: 'carbon:logo-github',
    color: '',
    desc: 'Не ждите возможности, создайте ее.',
    group: '开源组',
    date: '2021-04-01',
  },
  {
    title: 'Vue',
    icon: 'ion:logo-vue',
    color: '#3fb27f',
    desc: 'Вы сами определяете свое будущее.',
    group: '算法组',
    date: '2021-04-01',
  },
  {
    title: 'Html5',
    icon: 'ion:logo-html5',
    color: '#e18525',
    desc: 'Нет ничего важнее старания.',
    group: 'Отдыхающие на работе', // "上班摸鱼" -  "отдыхающие на работе"  более  точный  перевод  в  данном  контексте
    date: '2021-04-01',
  },
  {
    title: 'Angular',
    icon: 'ion:logo-angular',
    color: '#bf0c2c',
    desc: 'Страсть и желание могут преодолеть любые трудности.',
    group: 'UI',
    date: '2021-04-01',
  },
  {
    title: 'React',
    icon: 'bx:bxl-react',
    color: '#00d8ff',
    desc: 'Здоровое тело - это основа для достижения целей.',
    group: 'Технический профи', // "技术牛"  -  "Технический профи"  более  точный  перевод  в  данном  контексте
    date: '2021-04-01',
  },
  {
    title: 'Js',
    icon: 'ion:logo-javascript',
    color: '#4daf1bc9',
    desc: 'Путь прокладывают не фантазиями, а действиями.',
    group: 'Архитектурная группа', // "架构组"  -  "Архитектурная группа"  более  точный  перевод  в  данном  контексте
    date: '2021-04-01',
  },
];