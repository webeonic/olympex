import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: 'Описание',
    dataIndex: 'des',
    width: '80',
  },

  {
    title: 'Код',
    dataIndex: 'code',
    width: '80',
  },

  {
    title: 'Название',
    dataIndex: 'name',
    width: '80',
  },

]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: 'Название',
    field: 'name',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'Код',
    field: 'code',
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
    label: 'Название',
    colProps: {
      span: 24
    },
    field: 'name',
  },

  {
    component: 'InputNumber',
    label: 'Код',
    colProps: {
      span: 24
    },
    field: 'code',
  },

  {
    component: 'InputTextArea',
    label: 'Описание',
    colProps: {
      span: 24
    },
    field: 'des',
  },

]