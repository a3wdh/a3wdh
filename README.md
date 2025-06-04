- 👋 Hi, I’m @a3wdh
- 👀 I’m interested in flutter and ios
- 🌱 I’m currently learning flutter
- 💞️ I’m looking to collaborate on flutter app a junior developer 
- 📫 How to reach me a3wdh@icloud.com

## Viewing binary diffs

The environment used for this project does not show binary diffs by default.
To see a textual representation of changes to `.bin` files, configure Git to
use the helper script included in this repository:

```bash
git config diff.hexdiff.textconv "scripts/hexdiff.sh"
```

After running that command, `git diff` will display hex dumps for binary files,
making it easier to review their changes.

## Comparing binary files

For an immediate comparison of two binary files, use the helper script
`scripts/bindiff.py`:

```bash
python scripts/bindiff.py old.bin new.bin
```

This prints a unified diff of the hex representation of both files, allowing you
to inspect differences without needing additional tools.

<!---
a3wdh/a3wdh is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
