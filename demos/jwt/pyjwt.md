# pyjwt
```
pip install pyjwt[crypto]
```
在 pip 命令中，当一个包名后面跟着一个这样的方括号 [package_extra]，这表示你在安装该包时同时希望安装该包的特定可选功能或依赖。这里的 [crypto] 是一个 extras_require 的名字，它指定了 pyjwt 包额外的加密相关依赖。

对于 pyjwt[crypto]，这个选项特别指安装与加密相关的依赖，主要是为了支持更多的签名算法，特别是那些需要额外加密库的算法，比如 ECDSA 算法需要 cryptography 库。如果不指定 [crypto]，基础的 HS256 等算法可能可以正常工作，但一些高级或特定场景下需要的加密算法则可能因为缺少依赖而无法使用。


代码中应该先导入 `jwt` 模块，然后再使用其功能。正确的导入语句应该是：

```python
import jwt
import time
```

这段代码没有问题，因为它是在假设你已经按照之前的指导安装了 `PyJWT` 库之后进行的。在Python脚本或项目中，你需要先通过 `pip install pyjwt[crypto]` 安装 `PyJWT`，然后才能在代码中通过 `import jwt` 导入并使用它。

总结一下步骤：
1. **安装 PyJWT**: 在命令行中运行 `pip install pyjwt[crypto]`。
2. **导入 PyJWT**: 在你的Python脚本中使用 `import jwt` 来导入库。
3. **使用 PyJWT**：之后，你就可以像示例代码那样使用 `jwt.encode()` 和 `jwt.decode()` 等函数了。

这样，你就能在Python程序中创建和验证JWT了。

<br>

## pyjwt报错 ImportError: DLL load failed while importing _rust: 找不到指定的程序。
这个错误提示表明在尝试导入`PyJWT`库时遇到了问题，特别是与 Rust 相关的部分。这可能是因为`PyJWT`的新版本（从2.0.0开始）引入了对Rust的依赖来提升性能，而你的环境中可能遇到了Rust扩展加载失败的问题。

针对这个问题，你可以尝试以下几个解决步骤：

1. **降级PyJWT版本**：如果你不需要最新版PyJWT提供的特性，可以降级到不依赖Rust的版本。可以通过以下命令安装一个早期版本的PyJWT，例如1.7.1：
   ```bash
   pip uninstall pyjwt
   pip install pyjwt==1.7.1
   ```

2. **安装Rust工具链**：确保你的系统上安装了Rust编程语言及其Cargo包管理器。访问[Rust官方网站](https://www.rust-lang.org/tools/install)获取安装说明。

3. **重新安装PyJWT**：安装Rust后，尝试重新安装`PyJWT`。Python包应该能够正确编译Rust扩展了：
   ```bash
   pip uninstall pyjwt
   pip install pyjwt
   ```

4. **检查环境变量和系统路径**：确保Rust的编译工具（如`rustc`和`cargo`）所在的目录已经添加到了系统的PATH环境变量中。

5. **编译平台问题**：如果你使用的是Windows，确保安装了适用于Windows的Visual Studio Build Tools，因为它们提供了必要的C++编译工具。可以从[这里](https://visualstudio.microsoft.com/visual-cpp-build-tools/)下载。

6. **查看错误日志**：如果上述步骤都不能解决问题，查看更详细的错误日志可能会提供关于为何DLL加载失败的具体原因，从而可以采取更有针对性的解决措施。

如果问题依然存在，可能需要进一步调查具体的系统配置或考虑在开发者社区（如GitHub Issues或Stack Overflow）寻求帮助，那里可能会有其他用户遇到过类似问题并分享了解决方案。