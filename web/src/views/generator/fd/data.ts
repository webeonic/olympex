import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: 'Поле ввода',
    dataIndex: 'input_1',
    width: '80',
  },

  {
    title: 'Числовое поле ввода',
    dataIndex: 'input_number_2',
    width: '80',
  },

  {
    title: 'Выпадающий список',
    dataIndex: 'select_1',
    width: '80',
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
    label: 'Числовое поле ввода',
    field: 'input_number_2',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'Выпадающий список',
    field: 'select_1',
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
    itemProps: {
      labelCol: {},
      wrapperCol: {},
      required: true,
      message: 'Отправлено'
    },
    rules: [
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      }
    ]
  },
  {
    component: 'InputNumber',
    label: 'Числовое поле ввода',
    field: 'input_number_2',
    colProps: {
      span: 24
    },
    componentProps: {
      style: 'width:100%'
    },
    itemProps: {
      labelCol: {},
      wrapperCol: {
        span: 24
      }
    }
  },
  {
    component: 'Select',
    label: 'Выпадающий список',
    field: 'select_1',
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
      ],
      allowClear: false
    },
    itemProps: {
      labelCol: {},
      wrapperCol: {
        span: 24
      },
      required: false,
      message: 'Отправлено'
    },
    rules: [
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      }
    ]
  }
]