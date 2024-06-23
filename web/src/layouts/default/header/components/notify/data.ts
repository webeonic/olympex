export interface ListItem {
  id: string;
  avatar: string;
  // Заголовок уведомления
  title: string;
  // Показывать ли зачеркивание в заголовке
  titleDelete?: boolean;
  datetime: string;
  type: string;
  read?: boolean;
  description: string;
  clickClose?: boolean;
  extra?: string;
  color?: string;
}

export interface TabItem {
  key: string;
  name: string;
  list: ListItem[];
  unreadlist?: ListItem[];
}

export const tabListData: TabItem[] = [
  {
    key: '1',
    name: 'Уведомления',
    list: [
      {
        id: '000000001',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png',
        title: 'Вы получили 14 новых еженедельных отчетов',
        description: '',
        datetime: '2017-08-09',
        type: '1',
      },
      {
        id: '000000002',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/OKJXDXrmkNshAMvwtvhu.png',
        title: 'Ваша рекомендация Куньнини прошла третий раунд собеседования',
        description: '',
        datetime: '2017-08-08',
        type: '1',
      },
      {
        id: '000000003',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/kISTdvpyTAhtGxpovNWd.png',
        title: 'Этот шаблон может различать различные типы уведомлений',
        description: '',
        datetime: '2017-08-07',
        // read: true,
        type: '1',
      },
      {
        id: '000000004',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title: 'Левая иконка используется для различения различных типов',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
      {
        id: '000000005',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title:
          'Заголовок может автоматически отображать многоточие. В этом примере количество строк заголовка установлено в 1. Если содержимое превышает 1 строку, оно будет автоматически усечено, и будет доступен всплывающий текст с полным заголовком.',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
      {
        id: '000000006',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title: 'Левая иконка используется для различения различных типов',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
      {
        id: '000000007',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title: 'Левая иконка используется для различения различных типов',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
      {
        id: '000000008',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title: 'Левая иконка используется для различения различных типов',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
      {
        id: '000000009',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title: 'Левая иконка используется для различения различных типов',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
      {
        id: '000000010',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
        title: 'Левая иконка используется для различения различных типов',
        description: '',
        datetime: '2017-08-07',
        type: '1',
      },
    ],
  },
  {
    key: '2',
    name: 'Сообщения',
    list: [
      {
        id: '000000006',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/fcHMVNCjPOsbUGdEduuv.jpeg',
        title: 'Кулили прокомментировала вас',
        description: 'Описание информации. Описание информации. Описание информации',
        datetime: '2017-08-07',
        type: '2',
        clickClose: true,
      },
      {
        id: '000000007',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/fcHMVNCjPOsbUGdEduuv.jpeg',
        title: 'Чжу Пянью ответил вам',
        description: 'Этот шаблон используется для напоминания о том, кто взаимодействовал с вами.',
        datetime: '2017-08-07',
        type: '2',
        clickClose: true,
      },
      {
        id: '000000008',
        avatar: 'https://gw.alipayobjects.com/zos/rmsportal/fcHMVNCjPOsbUGdEduuv.jpeg',
        title: 'Заголовок',
        description:
          'Поместите курсор сюда, чтобы проверить, как обрабатываются очень длинные сообщения. В этом примере максимальное количество строк описания установлено в 2. Описание, превышающее 2 строки, будет усечено, а полный текст можно просмотреть с помощью всплывающего текста',
        datetime: '2017-08-07',
        type: '2',
        clickClose: true,
      },
    ],
  },
  {
    key: '3',
    name: 'Задачи',
    list: [
      {
        id: '000000009',
        avatar: '',
        title: 'Название задачи',
        description: 'Задача должна быть запущена до 2017-01-12 20:00',
        datetime: '',
        extra: 'Не начато',
        color: '',
        type: '3',
      },
      {
        id: '000000010',
        avatar: '',
        title: 'Неотложное изменение кода стороннего поставщика',
        description: 'Гуаньлинь должен завершить задачу изменения кода до 2017-01-07',
        datetime: '',
        extra: 'Истекает скоро',
        color: 'red',
        type: '3',
      },
      {
        id: '000000011',
        avatar: '',
        title: 'Экзамен по информационной безопасности',
        description: 'Назначить Жуэр завершить обновление и публикацию до 2017-01-09',
        datetime: '',
        extra: 'Затрачено 8 дней',
        color: 'gold',
        type: '3',
      },
      {
        id: '000000012',
        avatar: '',
        title: 'Публикация версии ABCD',
        description: 'Назначить Жуэр завершить обновление и публикацию до 2017-01-09',
        datetime: '',
        extra: 'В процессе',
        color: 'blue',
        type: '3',
      },
    ],
  },
];