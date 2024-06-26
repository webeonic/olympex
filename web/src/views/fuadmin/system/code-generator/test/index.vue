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
            {{ t("common.addText") }}
          </a-button>
          <a-button
              type="error"
              v-auth="['demo:delete']"
              preIcon="ant-design:delete-outlined"
              @click="handleBulkDelete"
          >
            {{ t("common.delText") }}
          </a-button>
          <BasicUpload
              :maxSize="20"
              :maxNumber="1"
              @change="handleChange"
              class="my-5"
              type="warning"
              :text="t('common.importText')"
              v-auth="['demo:update']"
          />
          <a-button
              type="success"
              v-auth="['demo:update']"
              preIcon="carbon:cloud-download"
              @click="handleExportData"
          >
            {{ t("common.exportText") }}
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
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                placement: 'left',
                auth: ['demo:delete'],
                popConfirm: {
                  title: t('common.delHintText'),
                  confirm: handleDelete.bind(null, record.id),
                },
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <Modal @register="registerModal" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

import { BasicTable, useTable, TableAction } from "/@/components/Table";
import { usePermission } from "/@/hooks/web/usePermission";
import { useModal } from "/@/components/Modal";

import { Space } from "ant-design-vue";
import { BasicUpload } from "/@/components/Upload";
// import { deleteItem, getList, exportData, importData } from "./api";
import { message } from "ant-design-vue";
import { downloadByData } from "/@/utils/file/download";
import { useI18n } from "/@/hooks/web/useI18n";
import Modal from "./modal.vue";

export default defineComponent({
  name: "Demo",
  components: {
    Modal
    , BasicTable, TableAction, BasicUpload, Space
  },
  setup() {
    const { t } = useI18n();
    const [registerModal, { openModal }] = useModal();

    // const { createConfirm } = useMessage();
    const { hasPermission } = usePermission();
    const [registerTable, { reload, getSelectRows }] = useTable({
      // api: getList,
      // columns,
      // formConfig: {
      //   labelWidth: 80,
      //   schemas: searchFormSchema
      // },
      useSearchForm: true,
      showTableSetting: true,
      tableSetting: { fullScreen: true },
      bordered: true,
      showIndexColumn: false,
      rowSelection: {
        type: "checkbox"
      },
      actionColumn: {
        width: 150,
        title: t("common.operationText"),
        dataIndex: "action",
        fixed: undefined
      }
    });

    function handleCreate() {
      openModal(true, {
        isUpdate: false
      });
    }

    function handleEdit(record: Recordable) {
      openModal(true, {
        record,
        isUpdate: true
      });
    }

    async function handleDelete(id: number) {
      // await deleteItem(id);
      message.success(t("common.successText"));
      await reload();
    }

    function handleBulkDelete() {
      // if (getSelectRows().length == 0) {
      //   message.warning(t("common.batchDelHintText"));
      // } else {
      //   createConfirm({
      //     iconType: "warning",
      //     title: t("common.hintText"),
      //     content: t("common.delHintText"),
      //     async onOk() {
      //       for (const item of getSelectRows()) {
      //         await deleteItem(item.id);
      //       }
      //       message.success(t("common.successText"));
      //       await reload();
      //     }
      //   });
      // }
    }

    async function handleChange(list: string[]) {
      console.log(list[0]);
      // await importData({ path: list[0] });
      message.success(`Импорт выполнен успешно`); // "导入成功" - "Импорт выполнен успешно"  более  точный  и  понятный  перевод  в  русском  языке
      await reload();
    }

    async function handleExportData() {
      // const response = await exportData();
      await downloadByData(response.data, "Данные проекта.xlsx"); // "项目数据.xlsx" - "Данные проекта.xlsx"  более  точный  и  понятный  перевод  в  русском  языке
    }

    function handleSuccess() {
      message.success(t("common.successText"));
      reload();
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
      t
    };
  }
});
</script>