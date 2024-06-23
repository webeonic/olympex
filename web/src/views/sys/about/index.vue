<template>
  <PageWrapper title="О проекте">
    <template #headerContent>
      <div class="flex justify-between items-center">
        <span class="flex-1">
          <a :href="GITHUB_URL" target="_blank">{{ name }}</a>
          — это бэкэнд-решение, основанное на Vue3.0, Vite, Ant-Design-Vue, TypeScript. Цель проекта — предоставить готовые решения «из коробки» и богатые примеры для разработки средних и крупных проектов, не ограничивая использование кода в коммерческих целях.
        </span>
      </div>
    </template>
    <Description @register="infoRegister" class="enter-y" />
    <Description @register="register" class="my-4 enter-y" />
    <Description @register="registerDev" class="enter-y" />
  </PageWrapper>
</template>
<script lang="ts" setup>
  import { h } from 'vue';
  import { Tag } from 'ant-design-vue';
  import { PageWrapper } from '/@/components/Page';
  import { Description, DescItem, useDescription } from '/@/components/Description/index';
  import { GITHUB_URL, SITE_URL, DOC_URL } from '/@/settings/siteSetting';

  const { pkg, lastBuildTime } = __APP_INFO__;

  const { dependencies, devDependencies, name, version } = pkg;

  const schema: DescItem[] = [];
  const devSchema: DescItem[] = [];

  const commonTagRender = (color: string) => (curVal) => h(Tag, { color }, () => curVal);
  const commonLinkRender = (text: string) => (href) => h('a', { href, target: '_blank' }, text);

  const infoSchema: DescItem[] = [
    {
      label: 'Версия',
      field: 'version',
      render: commonTagRender('blue'),
    },
    {
      label: 'Время последней сборки',
      field: 'lastBuildTime',
      render: commonTagRender('blue'),
    },
    {
      label: 'Адрес документации',
      field: 'doc',
      render: commonLinkRender('Документация'),
    },
    {
      label: 'Адрес демо',
      field: 'preview',
      render: commonLinkRender('Демо'),
    },
    {
      label: 'Github',
      field: 'github',
      render: commonLinkRender('Github'),
    },
  ];

  const infoData = {
    version,
    lastBuildTime,
    doc: DOC_URL,
    preview: SITE_URL,
    github: GITHUB_URL,
  };

  Object.keys(dependencies).forEach((key) => {
    schema.push({ field: key, label: key });
  });

  Object.keys(devDependencies).forEach((key) => {
    devSchema.push({ field: key, label: key });
  });

  const [register] = useDescription({
    title: 'Зависимости в продакшене',
    data: dependencies,
    schema: schema,
    column: 3,
  });

  const [registerDev] = useDescription({
    title: 'Зависимости в разработке',
    data: devDependencies,
    schema: devSchema,
    column: 3,
  });

  const [infoRegister] = useDescription({
    title: 'Информация о проекте',
    data: infoData,
    schema: infoSchema,
    column: 2,
  });
</script>