import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: 'Поле ввода',
    dataIndex: 'input_1',
    width: '80',
  },

  {
    title: 'Текстовое поле',
    dataIndex: 'input_text_area_2',
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
    label: 'Текстовое поле',
    field: 'input_text_area_2',
    component: 'Input',
    colProps: { span: 6 },
  },

];
export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },

  {
    component: 'Input',
    label: 'Поле ввода',
    colProps: {
      span: 24
    },
    field: 'input_1',
  },

  {
    component: 'InputTextArea',
    label: 'Текстовое поле',
    colProps: {
      span: 24
    },
    field: 'input_text_area_2',
  },

]