<template>
  <div>
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <Space style="height: 40px">
          <a-button
            type="primary"
            v-auth="['demo:add']"
            preIcon="ant-design:plus-outlined"
            @click="handleCreate"
          >
            {{ t('common.addText') }}
          </a-button>
          <a-button
            type="error"
            v-auth="['demo:delete']"
            preIcon="ant-design:delete-outlined"
            @click="handleBulkDelete"
          >
            {{ t('common.delText') }}
          </a-button>
        </Space>
      </template>
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <TableAction
            :actions="[
              {
                type: 'button',
                icon: 'clarity:note-edit-line',
                color: 'primary',
                auth: ['demo:update'],
                onClick: handleEdit.bind(null, record),
              },
              {
                type: 'button',
                icon: 'ant-design:export-outlined',
                color: 'success',
                auth: ['demo:update'],
                tooltip: 'Экспорт кода',
                popConfirm: {
                  title:
                    'Автоматическое создание меню и экспорт кода для фронтенда и бэкенда\n' +
                    'Фронтенд-путь: /views/generator\n' +
                    'Бэкенд-путь: /generator',
                  confirm: exportCode.bind(null, record.id),
                },
              },
              {
                type: 'button',
                icon: 'ant-design:caret-right-outlined',
                color: 'warning',
                auth: ['demo:update'],
                tooltip: 'Создать базу данных',
                popConfirm: {
                  title: 'Автоматическое создание схемы таблиц в базе данных',
                  confirm: createDB.bind(null, record.id),
                },
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <DesignModal @register="registerModal" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useModal } from '/@/components/Modal';

  import { Space } from 'ant-design-vue';
  import { BasicUpload } from '/@/components/Upload';
  import { deleteItem, getList, importData, codeGenerator, dbGenerator } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { downloadByData } from '/@/utils/file/download';
  import { useI18n } from '/@/hooks/web/useI18n';
  import DesignModal from '/@/views/fuadmin/system/code-generator/template/design/index.vue';

  export default defineComponent({
    name: 'GeneratorTemplate',
    components: {
      DesignModal,
      BasicTable,
      TableAction,
      BasicUpload,
      Space,
    },
    setup() {
      const { t } = useI18n();
      const [registerModal, { openModal }] = useModal();

      const { createConfirm } = useMessage();
      const { hasPermission } = usePermission();
      const [registerTable, { reload, getSelectRows }] = useTable({
        api: getList,
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
        },
        useSearchForm: true,
        showTableSetting: true,
        tableSetting: { fullScreen: true },
        bordered: true,
        showIndexColumn: false,
        rowSelection: {
          type: 'checkbox',
        },
        actionColumn: {
          width: 150,
          title: t('common.operationText'),
          dataIndex: 'action',
          fixed: undefined,
        },
      });

      function handleCreate() {
        openModal(true, {
          isUpdate: false,
        });
      }

      function handleEdit(record: Recordable) {
        openModal(true, {
          record,
          isUpdate: true,
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success(t('common.successText'));
        await reload();
      }

      function handleBulkDelete() {
        if (getSelectRows().length == 0) {
          message.warning(t('common.batchDelHintText'));
        } else {
          createConfirm({
            iconType: 'warning',
            title: t('common.hintText'),
            content: t('common.delHintText'),
            async onOk() {
              for (const item of getSelectRows()) {
                await deleteItem(item.id);
              }
              message.success(t('common.successText'));
              await reload();
            },
          });
        }
      }

      async function handleChange(list: string[]) {
        console.log(list[0]);
        await importData({ path: list[0] });
        message.success(`Импорт выполнен успешно`);
        await reload();
      }

      async function handleExportData() {
        const response = await exportData();
        await downloadByData(response.data, 'Данные проекта.xlsx');
      }

      function handleSuccess() {
        message.success(t('common.successText'));
        reload();
      }

      const exportData = (data: string, fileName: string) => {
        let content = 'data:text/csv;charset=utf-8,';
        content += data;
        console.log(content, 111);

        const encodedUri = encodeURI(content);
        const actions = document.createElement('a');
        actions.setAttribute('href', encodedUri);
        actions.setAttribute('download', fileName);
        actions.click();
      };

      async function exportCode(id: number) {
        await codeGenerator(id);
        message.success(t('common.successText'));
      }

      async function createDB(id: number) {
        await dbGenerator(id);
        message.success(t('common.successText'));
      }

      return {
        registerTable,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        hasPermission,
        handleBulkDelete,
        getSelectRows,
        handleExportData,
        handleChange,
        registerModal,
        exportCode,
        createDB,
        t,
      };
    },
  });
</script>