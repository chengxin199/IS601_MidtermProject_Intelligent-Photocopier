# 版本管理说明

## 自动版本递增（已启用）

每次 `git commit` 时会自动递增 patch 版本号（例如：1.0.1 → 1.0.2）。

**工作原理：**
- Git pre-commit hook 检测到代码变更
- 自动运行 `bump_version.py patch --quiet`
- 更新 `VERSION` 文件和 `Lessons/index.njk` 中的版本号
- 自动添加到当前 commit 中

**不需要任何手动操作！** 只需正常 commit 即可。

---

## 手动版本控制（需要时）

如果需要手动控制版本号（例如发布大版本）：

### Patch 版本（bug 修复）
```bash
python bump_version.py patch
# 1.0.1 → 1.0.2
```

### Minor 版本（新功能）
```bash
python bump_version.py minor
# 1.0.2 → 1.1.0
```

### Major 版本（破坏性变更）
```bash
python bump_version.py major
# 1.1.0 → 2.0.0
```

### 预览变更（不实际修改）
```bash
python bump_version.py patch --dry-run
```

### 静默模式（用于自动化）
```bash
python bump_version.py patch --quiet
```

---

## 禁用自动版本递增

如果不想要自动版本递增，删除 Git hook：

```bash
rm .git/hooks/pre-commit
```

---

## 当前版本

查看当前版本：
```bash
cat VERSION
```

版本会显示在网站底部的 footer 中。
