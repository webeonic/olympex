export default {
  api: {
    operationFailed: 'Операция не удалась',
    errorTip: 'Ошибка',
    errorMessage: 'Операция не удалась, произошла ошибка системы!',
    timeoutMessage: 'Время сеанса истекло, пожалуйста, войдите снова!',
    apiTimeoutMessage: 'Превышено время ожидания запроса к API, пожалуйста, обновите страницу и попробуйте снова!',
    apiRequestFailed: 'Ошибка запроса, пожалуйста, повторите попытку позже',
    networkException: 'Ошибка сети',
    networkExceptionMsg: 'Ошибка сети, проверьте, подключено ли ваше интернет-соединение!',

    errMsg401: 'Пользователь не авторизован (ошибка токена, имени пользователя или пароля)!',
    errMsg403: 'Извините, у вас нет прав доступа!',
    errMsg404: 'Ошибка сетевого запроса, ресурс не найден!',
    errMsg405: 'Ошибка сетевого запроса, метод запроса не разрешен!',
    errMsg408: 'Превышено время ожидания сетевого запроса!',
    errMsg500: 'Ошибка сервера, обратитесь к администратору!',
    errMsg501: 'Сеть не реализована!',
    errMsg502: 'Ошибка сети!',
    errMsg503: 'Сервис недоступен, сервер временно перегружен или находится на обслуживании!',
    errMsg504: 'Превышено время ожидания сети!',
    errMsg505: 'Версия HTTP не поддерживает этот запрос!',
  },
  app: { logoutTip: 'Напоминание', logoutMessage: 'Вы действительно хотите выйти из системы?', menuLoading: 'Загрузка меню...' },
  errorLog: {
    tableTitle: 'Список ошибок',
    tableColumnType: 'Тип',
    tableColumnDate: 'Время',
    tableColumnFile: 'Файл',
    tableColumnMsg: 'Сообщение об ошибке',
    tableColumnStackMsg: 'Информация об стеке',

    tableActionDesc: 'Подробности',

    modalTitle: 'Подробности ошибки',

    fireVueError: 'Нажмите, чтобы вызвать ошибку Vue',
    fireResourceError: 'Нажмите, чтобы вызвать ошибку загрузки ресурса',
    fireAjaxError: 'Нажмите, чтобы вызвать ошибку Ajax',

    enableMessage: 'Действует только при useErrorHandle = true в `/src/settings/projectSetting.ts`.',
  },
  exception: {
    backLogin: 'Вернуться к входу',
    backHome: 'Вернуться на главную',
    subTitle403: 'Извините, у вас нет прав доступа к этой странице.',
    subTitle404: 'Извините, страница не найдена.',
    subTitle500: 'Извините, на сервере произошла ошибка.',
    noDataTitle: 'На этой странице нет данных',
    networkErrorTitle: 'Ошибка сети',
    networkErrorSubTitle: 'Извините, ваше интернет-соединение разорвано. Проверьте ваше подключение!',
  },
  lock: {
    unlock: 'Нажмите, чтобы разблокировать',
    alert: 'Неверный пароль блокировки',
    backToLogin: 'Вернуться к входу',
    entry: 'Войти в систему',
    placeholder: 'Введите пароль блокировки или пароль пользователя',
  },
  login: {
    backSignIn: 'Назад',
    signInFormTitle: 'Вход',
    mobileSignInFormTitle: 'Вход по номеру телефона',
    qrSignInFormTitle: 'Вход с помощью QR-кода',
    signUpFormTitle: 'Регистрация',
    forgetFormTitle: 'Сброс пароля',

    signInTitle: 'Python Backend Management System',
    signInDesc: 'Разработано с использованием Django Ninja на бэкенде',
    policy: 'Я согласен с политикой конфиденциальности xxx',
    scanSign: 'Отсканируйте код и нажмите "Подтвердить", чтобы завершить вход',

    loginButton: 'Вход',
    registerButton: 'Регистрация',
    rememberMe: 'Запомнить меня',
    forgetPassword: 'Забыли пароль?',
    otherSignIn: 'Другие способы входа',

    // notify
    loginSuccessTitle: 'Вход выполнен успешно',
    loginSuccessDesc: 'Добро пожаловать обратно',

    // placeholder
    accountPlaceholder: 'Введите учетную запись',
    passwordPlaceholder: 'Введите пароль',
    smsPlaceholder: 'Введите код подтверждения',
    mobilePlaceholder: 'Введите номер телефона',
    policyPlaceholder: 'Установите флажок, чтобы зарегистрироваться',
    diffPwd: 'Пароли не совпадают',

    userName: 'Учетная запись',
    password: 'Пароль',
    confirmPassword: 'Подтвердите пароль',
    email: 'Почта',
    smsCode: 'SMS-код',
    mobile: 'Номер телефона',
  },
};