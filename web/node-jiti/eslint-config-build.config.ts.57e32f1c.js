"use strict";Object.defineProperty(exports, "__esModule", { value: true });exports.default = void 0;var _unbuild = require("unbuild");var _default =

(0, _unbuild.defineBuildConfig)({
  clean: true,
  entries: ['src/index', 'src/strict'],
  declaration: true,
  rollup: {
    emitCJS: true
  }
});exports.default = _default; /* v7-3111e0eb06a3fb7d */