
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: 'Поле ввода',
    dataIndex: 'input_1',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['test:input_1'],
    resizable: true,
  },

  {
    title: 'Текстовое поле',
    dataIndex: 'input_text_area_2',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['test:input_text_area_2'],
    resizable: true,
  },

  {
    title: 'Выпадающий список',
    dataIndex: 'select_3',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['test:select_3'],
    resizable: true,
  },

]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: 'Поле ввода',
    field: 'input_1',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'Текстовое поле',
    field: 'input_text_area_2',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'Выпадающий список',
    field: 'select_3',
    component: 'Input',
    colProps: { span: 6 },
  },

];
export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false
  },
  {
    component: 'Input',
    label: 'Поле ввода',
    field: 'input_1',
    colProps: {
      span: 24
    },
    componentProps: {
      type: 'text'
    },
    itemProps: {}
  },
  {
    component: 'InputTextArea',
    label: 'Текстовое поле',
    field: 'input_text_area_2',
    colProps: {
      span: 24
    },
    componentProps: {},
    itemProps: {}
  },
  {
    component: 'Select',
    label: 'Выпадающий список',
    field: 'select_3',
    colProps: {
      span: 24
    },
    componentProps: {
      options: [
        {
          label: 'Вариант 1',
          value: '1'
        },
        {
          label: 'Вариант 2',
          value: '2'
        }
      ]
    },
    itemProps: {}
  }
]