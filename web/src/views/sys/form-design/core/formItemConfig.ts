/**
 * @description：Конфигурация формы
 */
import { IVFormComponent } from '../typings/v-form-component';
import { isArray } from 'lodash-es';
import { componentMap as VbenCmp, add } from '/@/components/Form/src/componentMap';
import { ComponentType } from '/@/components/Form/src/types';

import { componentMap as Cmp } from '../components';
import { Component } from 'vue';

const componentMap = new Map<string, Component>();

// Если есть другие элементы управления, их можно инициализировать здесь

// Регистрация библиотек элементов управления Ant
Cmp.forEach((value, key) => {
  componentMap.set(key, value);
  if (VbenCmp[key] == null) {
    add(key as ComponentType, value);
  }
});
// Регистрация библиотек элементов управления Vben
VbenCmp.forEach((value, key) => {
  componentMap.set(key, value);
});

export { componentMap };

/**
 * Настройка пользовательских элементов управления формой
 * @param {IVFormComponent | IVFormComponent[]} config
 */
export function setFormDesignComponents(config: IVFormComponent | IVFormComponent[]) {
  if (isArray(config)) {
    config.forEach((item) => {
      const { componentInstance: component, ...rest } = item;
      componentMap[item.component] = component;
      customComponents.push(Object.assign({ props: {} }, rest));
    });
  } else {
    const { componentInstance: component, ...rest } = config;
    componentMap[config.component] = component;
    customComponents.push(Object.assign({ props: {} }, rest));
  }
}

// Пользовательские элементы управления, установленные снаружи
export const customComponents: IVFormComponent[] = [];

// Список элементов управления слева и их начальные атрибуты
// props.slotName, генерирует слот на уровне formitem и связывает его с текущим значением record
// Атрибут props, тип - объект, не может быть undefined или null.
export const baseComponents: IVFormComponent[] = [
  // {
  //   component: 'InputCountDown',
  //   label: 'Ввод обратного отсчета',
  //   icon: 'line-md:iconify2',
  //   colProps: { span: 24 },
  //   field: '',
  //   componentProps: {},
  // },
  {
    component: 'Input',
    label: 'Поле ввода',
    icon: 'bi:input-cursor-text',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      type: 'text',
    },
  },
  {
    component: 'InputNumber',
    label: 'Числовое поле ввода',
    icon: 'ant-design:field-number-outlined',
    field: '',
    colProps: { span: 24 },
    componentProps: { style: 'width:200px' },
  },
  {
    component: 'InputTextArea',
    label: 'Текстовое поле',
    icon: 'ant-design:file-text-filled',
    field: '',
    colProps: { span: 24 },
    componentProps: {},
  },
  {
    component: 'CheckboxGroup',
    label: 'Группа флажков',
    icon: 'ant-design:check-circle-filled',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      options: [
        {
          label: 'Вариант 1',
          value: '1',
        },
        {
          label: 'Вариант 2',
          value: '2',
        },
      ],
    },
  },

  {
    component: 'Select',
    label: 'Выпадающий список',
    icon: 'gg:select',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      options: [
        {
          label: 'Вариант 1',
          value: '1',
        },
        {
          label: 'Вариант 2',
          value: '2',
        },
      ],
    },
  },
  {
    component: 'IconPicker',
    label: 'Выбор иконки',
    icon: 'line-md:iconify2',
    colProps: { span: 24 },
    field: '',
    componentProps: {},
  },
  {
    component: 'StrengthMeter',
    label: 'Прочность пароля',
    icon: 'wpf:password1',
    colProps: { span: 24 },
    field: '',
    componentProps: {},
  },
  // {
  //   component: 'AutoComplete',
  //   label: 'Автозаполнение',
  //   icon: 'wpf:password1',
  //   colProps: { span: 24 },
  //   field: '',
  //   componentProps: {
  //     placeholder: 'Введите регулярное выражение',
  //     options: [
  //       {
  //         value: '/^(?:(?:\\+|00)86)?1[3-9]\\d{9}$/',
  //         label: 'Номер мобильного телефона',
  //       },
  //       {
  //         value: '/^((ht|f)tps?:\\/\\/)?[\\w-]+(\\.[\\w-]+)+:\\d{1,5}\\/?$/',
  //         label: 'URL-адрес с номером порта',
  //       },
  //     ],
  //   },
  // },
  {
    component: 'Divider',
    label: 'Разделитель',
    icon: 'radix-icons:divider-horizontal',
    colProps: { span: 24 },
    field: '',
    componentProps: {
      orientation: 'center',
      dashed: true,
    },
  },
  // {
  //   component: 'Checkbox',
  //   label: 'Флажок',
  //   icon: 'ant-design:check-circle-outlined',
  //   colProps: { span: 24 },
  //   field: '',
  // },

  // {
  //   component: 'Radio',
  //   label: 'Радиокнопка',
  //   icon: 'ant-design:check-circle-outlined',
  //   field: '',
  //   colProps: { span: 24 },
  //   componentProps: {},
  // },
  {
    component: 'RadioGroup',
    label: 'Группа радиокнопок',
    icon: 'carbon:radio-button-checked',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      options: [
        {
          label: 'Вариант 1',
          value: '1',
        },
        {
          label: 'Вариант 2',
          value: '2',
        },
      ],
    },
  },
  {
    component: 'DatePicker',
    label: 'Выбор даты',
    icon: 'healthicons:i-schedule-school-date-time-outline',
    field: '',
    colProps: { span: 24 },
    componentProps: {},
  },
  {
    component: 'RangePicker',
    label: 'Диапазон дат',
    icon: 'healthicons:i-schedule-school-date-time-outline',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      placeholder: ['Начальная дата', 'Конечная дата'],
    },
  },
  {
    component: 'MonthPicker',
    label: 'Выбор месяца',
    icon: 'healthicons:i-schedule-school-date-time-outline',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      placeholder: 'Выберите месяц',
    },
  },
  {
    component: 'TimePicker',
    label: 'Выбор времени',
    icon: 'healthicons:i-schedule-school-date-time',
    field: '',
    colProps: { span: 24 },
    componentProps: {},
  },
  {
    component: 'Slider',
    label: 'Ползунок',
    icon: 'vaadin:slider',
    field: '',
    colProps: { span: 24 },
    componentProps: {},
  },
  {
    component: 'Rate',
    label: 'Рейтинг',
    icon: 'ic:outline-star-rate',
    field: '',
    colProps: { span: 24 },
    componentProps: {},
  },
  {
    component: 'Switch',
    label: 'Переключатель',
    icon: 'entypo:switch',
    field: '',
    colProps: { span: 24 },
    componentProps: {},
  },
  {
    component: 'TreeSelect',
    label: 'Дерево выбора',
    icon: 'clarity:tree-view-line',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      treeData: [
        {
          label: 'Вариант 1',
          value: '1',
          children: [
            {
              label: 'Вариант 3',
              value: '1-1',
            },
          ],
        },
        {
          label: 'Вариант 2',
          value: '2',
        },
      ],
    },
  },
  {
    component: 'Upload',
    label: 'Загрузка',
    icon: 'ant-design:upload-outlined',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      api: () => 1,
    },
  },
  {
    component: 'Cascader',
    label: 'Каскадный выбор',
    icon: 'ant-design:check-outlined',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      options: [
        {
          label: 'Вариант 1',
          value: '1',
          children: [
            {
              label: 'Вариант 3',
              value: '1-1',
            },
          ],
        },
        {
          label: 'Вариант 2',
          value: '2',
        },
      ],
    },
  },
  // {
  //   component: 'Button',
  //   label: 'Кнопка',
  //   icon: 'dashicons:button',
  //   field: '',
  //   colProps: { span: 24 },
  //   hiddenLabel: true,
  //   componentProps: {},
  // },
  // {
  //   component: 'ColorPicker',
  //   label: 'Выбор цвета',
  //   icon: 'carbon:color-palette',
  //   field: '',
  //   colProps: { span: 24 },
  //   componentProps: {
  //     defaultValue: '',
  //     value: '',
  //   },
  // },

  {
    component: 'slot',
    label: 'Слот',
    icon: 'vs:timeslot-question',
    field: '',
    colProps: { span: 24 },
    componentProps: {
      slotName: 'slotName',
    },
  },
];

// https://next.antdv.com/components/transfer-cn
const transferControl = {
  component: 'Transfer',
  label: 'Перемещение',
  icon: 'bx:bx-transfer-alt',
  field: '',
  colProps: { span: 24 },
  componentProps: {
    render: (item) => item.title,
    dataSource: [
      {
        key: 'key-1',
        title: 'Заголовок 1',
        description: 'Описание',
        disabled: false,
        chosen: true,
      },
      {
        key: 'key-2',
        title: 'title2',
        description: 'description2',
        disabled: true,
      },
      {
        key: 'key-3',
        title: 'Заголовок 3',
        description: 'Описание 3',
        disabled: false,
        chosen: true,
      },
    ],
  },
};

baseComponents.push(transferControl);

export const layoutComponents: IVFormComponent[] = [
  {
    field: '',
    component: 'Grid',
    label: 'Сетка',
    icon: 'icon-grid',
    componentProps: {},
    columns: [
      {
        span: 12,
        children: [],
      },
      {
        span: 12,
        children: [],
      },
    ],
    colProps: { span: 24 },
    options: {
      gutter: 0,
    },
  },
];